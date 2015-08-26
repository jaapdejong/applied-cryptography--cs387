#!/usr/bin/python

# For this problem, Alice and Bob want to communicate
# They have set up two servers to respond to messages
# and you need to transfer the messages between the two.
#
# The protocol goes as follows:
# 1) a. Establish a session with Alice
#    b. Establish a session with Bob
# 2) a. Send Alice's public information to Bob
#    b. Send Bob's public information to Alice
# 3) Relay messages
#
# Step 1 - Establishing a session
# The function `initialize` can be used to establish a session.
# Alice responds to a POST request with the `type` key set to "init".
# She will send back two values: a token which is used to track the 
# session and a public value, g^x.  The token will expire after 20 minutes,
# so you will need to re-initialize a session after that time
#
# Step 2 - Exchanging public information
# Alice now needs Bob's public value.  The function `send_key` can be
# used to send this.  The function makes a POST request.  Alice responds with 
# a successful status.
#
# Step 3 - Relay messages
# Now that Alice and Bob have a shared secret key, they can use that
# to encrypt secret messages.  You will need to relay these messages.
# Use the `recieve_msg` function to get the first message to send from Alice
# Then, take the values recieved from that and send them to Bob, who will
# respond.  Take his response and send it back to Alice.  Repeat.
#
# Errors
# If you try to do something that Alice and Bob don't like, for example sending a message
# without first exchanging public information, they will respond with 
# a 501 status code and more information in the response.
#
# As with the challenge problem of Unit 5, this assignment requires that
# you run code on your own environment.  It will not work if you write
# code in the Udacity IDE and hit RUN or SUBMIT.
#
# You're allowed to use whatever programming language you want.  The 
# code provide below can be used as a reference implementation.
#

from urllib import urlopen, urlencode
import json

base = "http://cs387.udacity-extras.appspot.com/final"
Alice = base + "/alice"
Bob = base + "/bob"

def check_output(output):
    data = output.read()
    if output.getcode() != 200:
        raise Exception(data)
    data = json.loads(data)
    return data

def get_pg():
    output = urlopen(base)
    data = check_output(output)
    # returns {"p":<large prime>, "g":<generator for p>}
    return data

def initialize(person):
    data = {'type':'init'}
    output = urlopen(person, urlencode(data))
    data = check_output(output)
    # returns a dictionary 
    # {"token":<token_value>, "public": <g^x>}
    return data

def send_key(person, token, public, name):
    """
    person: url of Alice/Bob
    token: token used to track session
    public: the public value of the other party
    name: the name of the other party - "alice", "bob"
    """
    data = {'type':'key',
            'token':token,
            'public':public,
            'name':name}
    output = urlopen(person, urlencode(data))
    data = check_output(output)
    # Should be a response {"status":"success"}
    return data

def recieve_msg(person, token):
    data = {'type':'msg',
            'token':token}
    output = urlopen(person, urlencode(data))
    data = check_output(output)
    # should be a response
    # {"msg":<cipher>, "iv":<initialization vector>}
    return data

def send_msg(person, token, cipher, iv):
    data = {'type':'msg',
            'token':token,
            'message':cipher,
            'iv':iv}
    output = urlopen(person, urlencode(data))
    data = check_output(output)
    # If the person doesn't have
    # a response to the message, the response will
    # just be {"status":"success"}
    # else, the response will be {"status":"success", 
    #                             "reply":{"msg":<cipher>,
    #                                      "iv":<initialization vector>}}
    return data

def test():
 	### step 1a - Establish a session with Alice
	dictionaryAlice = initialize(Alice)				# --> {"token":<token_value>, "public": <g^x>}
	tokenAlice = dictionaryAlice['token']
	publicAlice = dictionaryAlice['public']

	### step 1b - Establish a session with Bob
	dictionaryBob = initialize(Bob)					# --> {"token":<token_value>, "public": <g^x>}
	tokenBob = dictionaryBob['token']
	publicBob = dictionaryBob['public']

	### step 2a - Send Alice's public information to Bob
	responseBob = send_key(Bob, tokenAlice, publicAlice, "alice")	# --> {"status":"success"}
	assert responseBob['status'] == 'success'
	
	### step 2b - Send Bob's public information to Alice
	responseAlice = send_key(Alice, tokenBob, publicBob, "bob")	# --> {"status":"success"}
	assert responseAlice['status'] == 'success'
	
	### step 3 - Relay messages
	msg = recieve_msg(Alice, tokenBob)				# --> {"msg":<cipher>, "iv":<initialization vector>}
	print msg
	cipher = msg['msg']
	iv = msg['iv'] 
	while True:
		msg = send_msg(Alice, tokenBob, cipher, iv)		# --> {"status":"success" ["reply":{"msg":<cipher>, "iv":<initialization vector>}}
		print msg
		if not ('reply' in msg): continue
		reply = msg['reply']
		if reply == None: break
		cipher = reply['msg']
		iv = reply['iv']
		
		msg = send_msg(Bob, tokenBob, cipher, iv)
		print msg
		reply = msg['reply']
		if reply == None: break
		cipher = reply['msg']
		iv = reply['iv']
		
			 
		

test()
