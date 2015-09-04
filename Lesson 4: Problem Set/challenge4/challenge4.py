#!/usr/bin/python

# HW4-Challenge Problem Version 2
#
# Here are 16 intercepted public keys (e, n) and
# associated cipher texts.  Your assignment is to
# decode as many as you can.  Some of them are 
# weak and should be easy to decode (see lecture 22) 
# and some of them are very difficult.
#
# You might also want to research known attacks on
# RSA for ideas on weak keys, messages and padding
#
# Although it is possible to decrypt all 16 message
# only 6 are necessary to get this problem correct.
# Getting at least 11 right would be a double challenge 
# problem. And getting all 16 right means we made a mistake.
#
# To discuss the challenge problem
# http://forums.udacity.com/cs387-april2012/questions/2814/hw4-6-challenge-question-discussion
#
# If you want to use functions from unit4_util, make sure to set the ASCII_BITS = 8
# import unit4_util
# unit4_util.ASCII_BITS = 8
#
# unit4_util code: http://pastebin.com/Te2AmDre

################
e0 = 65537
n0 = 116436872704204817262873499608558046190724591466716177557829773662807162485791977636521167560986434993048860346504247233074117974671540999410485959711510256117299326339754889488213509449940603119123994148576130959569697235313003024809821145961963221161561975123663333322412762102191502543834949106445222007561
cipher0 = "<\xad\xdd\xedg\x8b\x12\x0b\x00y\xa2\xf0\x86\xcbF\xf0\x8f\xb4~\xbd\x04\xd9\xac6iwxk\xcfi\xc4Z1p\\\x14\xa4rL\x9a#\x9f\xbf~\xec[\x8d\xfc(\x82\xc2s\xb9\x0e\xec(\xd9.}\xc5\xdf\xa8'`\xa5\xdb\x18\xf1Z\xff\x82xQJa\x11\x98/x&{\x0b\x17\xb9\xb1\x88\x8f\x85B\x7fH\xdbX\x9aV\x9a\xaf\x0fKc+\xf7?\xb8\xb4\x1fo\x0eeI\xa9\x90\x11\x83\xb8\xfdaMwM\xc7\xb48&-\xe8\xf1C"
m0 = 'But heard, half-heard, in the stillness'
################

################
e1 = 3
n1 = 131776503472993446247578652375782286463851826883886018427615607890323792437218636575447994626809806013420405963813337101556738852432247872506699457038044621191649758706817663135648397013226104530751563478671698441687437700125203966101608457556637550910814187779205610883544935666685906870199595346450733709263
cipher1 = '\x04\xacq#E/\xf4X\x126\xef\xc6\xb1\xfc\x10p*\x98P\xde\x089K\x16y0\xfa\xde\x9f\x05\x15+\xa3\x0f\xbc3\xd1t\xe7\x9a\x1b\x04m\xa1\x12\x96\x18Y\xf9\xc95\xce\x19 E\xfa\xe1\xb5\x8a\xd5\xf2\x99\xa6"<\xcb\x1a\xd0\xce=\x91\xfbw\t\xb5'
m1 = 'Chinese Remainder Theorem'
################

################
e2 = 3
n2 = 65659232975830381768328338666607829001259240689809015666589078261348261561917417083788447204534665997091584936794919521220643455263371034991817572752104164283083678838816431044389236958346474896965382016943200300407371205608596328649170408446414718769422147103617311701247139971805834487439320773304455320217
cipher2 = '\x04\xe97r\x13\x99\xf7\x80m\x19\xe3f\x1a\x92]u!\x17\xdf\xa8\xfd\xd4\xd0\xbea\xe8\x1f\xefc\xd6\xc7\xbf\xce\xa4q\xfe\xa4S\xff\xaf\x1aX\xc13g\xeb\x12\xadw\x17T\x05\x1c\x8e\xd8\xea\x1bkc\xd3\xfctQt\x8e\xf6d\x1a\x98\xbc}\x08\x1d%\xc7\xd2K\xb4\xa8\x96\xcf\x98D\x8a\xbd\xa7\xd2\xcc\x861$\xd1\x1b\xdd\xa0h\x83\xdan\xcbm\xa4\xf9\xef\x96\x12\x9c|\xc9\xd7\t\x9b\x0f:\x9e\xe0\xa1\xb2\t\x8b\x9d\x18\x07\x8e]\x8c\x13\xa2'
m2 = 'we recommend you read this blog: http://goo.gl/5I1lt'
################

################
e3 = 65537
n3 = 123740725722669778168140279746885116465689142044964932919259424632700251889210648897122745920893520079240373449556169792134756802777276891302849411753547670256331297747426561365967232060486102273866172732652784207074573713156422288123095681033001477048754016167961689427177649034193069903791184066398335275979
cipher3 = "\x96\x81\xd11'\xf26\xbfRx\x85\xfa*{l\xa0\xf9gN\xd5\xe1\x89\xe1$$\x0c\r\xa6\xb0\x12^X\x19gQt\xe4\xca\xb2`\xccO\xdf\xb4*\\\x12\x94\xa8\x07\xc8V2\xf2\xfa\xbd\x0f\xd9b%{\x18\x04Q\xebM\xaa\x996\xe7\xb2\xf4;\x8a\xa3\xd6t\xefi^\x9f}\xb6\xa5\xf3\xc7\x86M~b@\x06V\xa62\x99\xd5R\xb7\xaa\x8a\xd2\xd8p\xc6\xf0MU\xaf:(\xea\xa6d6!\xbb\xcd\xf96\xed\x13\xbe\xb4\xc6\x80i'"
m3 = ''#YOUR ANSWER HERE
################

################
e4 = 65537
n4 = 174231520673917075824734399421338044182598066866708821622792727890359025900245087848242723006461374386260651831496339387219798450553867568952404714118529459572066590008168303790157469082308091580819932970387450957047496109838586484814686040623994413943943700280260903054123602347796276801896181827746424409349
cipher4 = '\x8d\x15\x19\xdb\xa2b%\xa8\xf9r\xe1s\xd1\xb9\x91\x01\xac\xa5\xdbU\xac,\xcb\x89\x88\xf1i\xac\xdcC\x9dE\x18\xfeQ\xd9\xb9\xa8\xa8\x16\xafP\xdc\xd5B\x86\xb4)tK\x99\xd3\x7f\x88/\xa2\x90\xdf\xcc\x98\xa1l\xfd\xc7\xfa\x1f\xcd\x82\x1a\xf3\x98*\xb1e\xcd\xb2\xde\xae\xd6\xe8\x93hYEw?\x10\xde\xa9\x18\xc6&H\xebl\xb1\x98\x02)\x06\xf2\r\x9c`\x008\x13\xc1\xa1@\x15\x07\xf5|\x96\xdd\x84\xbd\xf9{\x8ee \xc7\x063\xb5\xb5'
m4 = 'Over the wintry forest, winds howl in rage'
################

################
e5 = 65537
n5 = 154624207324797376435320332790580937936761022444524329745992492506088072002504225456113354046488778813916771666944276555736671617396500696410754570132980562875859056165807630016963181226874989658340550960200466121814971000456664135187049322544510139273708052345814650574505699754914795663074450228533543056817
cipher5 = "i\xcf\xd3\xcd7.\xc8\xd5\x1f?\xbdtr0&z3\x1d\xf0\xe9p\xf3<YI\x80\xb0\xea3 \xb1\xda\x8e\n\x10m*\xe2\xceE\xbbi\x9c\xb5\x92\xaaMU\xe9\x1a)\x98\x07\x85\x99\xb9V\\\xbfyd\xf4T\xb3\x93\xe3N\xd8\xbd\xd8F\xde\x86Ep\xc0\xef\xd7\xe8\xc4\xf4\x80e\x16x\xcbQ\tV\xc3\xc8\xa4E\x95\xcf\x0e\xd3\\\t\xa2H\xd9\x85$vmC\x9b`\xc0\x93O MG\x0c'\xd6}\xbc\x8fO\xb6V\xcc\x1a\xcb\xc0"
m5 = ''#YOUR ANSWER HERE
################

################
e6 = 65537
n6 = 55658068259817811076952882351578415862870549608181369915628312865059323413004471043604703276316691018017425203301601197751731990108856534305858079813650908006137207122255581819587501300907072084616440442796887872335687503995776108872819766599926331124483312046239535167770356141832350688609707163033799579957
cipher6 = '",G\xae\xb7\x96 z=Y\xf3\x19\x11g\x9eA(\x8e\xa8J\x89\x86u\xb1\xd7\x8f\x86\x1e\x94\xc1GkE\xc8\x03\xe0\xb3LGN\x14\x81\xb2,\xc5\x04Z,\xe4\xf7Z\xdf\x91Z\x97\x1b]\x80\x06\xb4<\xc3x\xab\x83\x85o\x9e\x0bK\xca\x15c\x8c.O\xfb\x84\xbd>\x08\xd7\xff\r\xa6P\x86\x87)\x076\x9b\xdc\xe2\xf1\xe1`/0m\x84f\xb5\x9a\x83\xcc\xd7\x0eC\xae)\xcc\xff\xf3$<\xd6G\x17 \xb1\xd1\xe7\x1a\x0c\xac\x15\x90'
m6 = 'Between two waves of the sea. -T.S. Eliot'
################

################
e7 = 65537
n7 = 142790458604757964122637252257956461175023701838768573868119604983049820652820576222661702788815905296939051322350625332330328946814137523526132844748550060162093126006443484056742183764004234747175547357975153233786228275781507259080966207713629148725792124704247615358292708458914175756855275828988145447879
cipher7 = "\xc7\x7f\x91'Y'\xc6_\x91N\xa4\x0e\xe0\x83PX\xe1\xd2O\xf3\xff\x1e\x95\xc5{&\x07\xd7O9\x82;\xf0U9\xf1\x9b\x9a\x8d\x1b+cX\x17-X\xc7\xb0,\xe4Z0\x84PP\x89\xbf\xa4\xc3\xf6\xa2\xec\xdf\xf3\xca\x86\xc4\xad\xcfQ\xcf\xbcW\xd9m\xb2T\x98\x9dWu\xab\x8f\xe3\x91\xccL@\x89\xcf\xcc\x1f\xed>\x98\\\x02\xefE\x84\xa3t\x1d\xd3\xf8(PkO\x17q\xf7\xafX\x10S\x94\xdf\x9a*\xbc\xb3\x00\xecYa\xc2\x16"
m7 = ''#YOUR ANSWER HERE
################

################
e8 = 3
n8 = 105242314862613403128618012971241387248892052783002974105856821061278607957729115063535600558210614458208545471459242061573520534172108013775924181710251914675571061791713994144059933046151548906145029415704879628926489802957314522493622596489433179478769931611554984108813301116133814976882152241405085792401
cipher8 = '!t\x1fF\x81\xc3\x84m\x96z_\xaf\xcf[\xbbt\xef\xac\xf7\xc9]\xebaw\x06\x0e\x8ey\\H_\xee0B\xbaB?\xa9-4\x1cd\x16\xa4\x85\xeaOO\xda\xf8\x8e;\xdbY\xb6b\xf7|\xaf\x13\xa9\xba\x9a\xc5i\xa7f\x94\x80HJ^-\x80\x96\xd9\xb5\x1e\x9b5\x1c\xe2\xfa\xbc\xb3\xb5\xfa\xffIq\xabt$\x10\x01K\xef[;\x04T\x17\n\xbf\xa7\xb4\x0fr2\x19\xc43\x19\xa9\xac\xbb\x82Y\xf4X%\x8f\x0bd\x81\xa7n\xce'
m8 = 'we recommend you read this blog: http://goo.gl/5I1lt'
################

################
e9 = 3
n9 = 72119364642335338558230934777058054962694972953443182639333046521176125046406938854054638169330108689724380250570350428800376971990405399883726478777738596059986080075671524555383338963957060973245384873014181662159740775682510335778372893164426839838949550467826086219705472573462606617295335262085826901917
cipher9 = 'B\xc1\xd9EH\x8b\xc9D_s\x17\x90uGd\xb6\x10F\x16\xab\x1aN=t\\\xb6\xaa\xf6\x97\xd6\x17\xab&\xd1 Z\x82\xac\xc0wVw|\xa8\xf4\x8dxG\xb7Og\x8b\x8au?\x8c\xe3(\x0c\xec+\x0c\xc3\x8a\xe8k\x8f\x00\xc1\xf8\x95*\xe5\n\xc8fm\xdd\xcbIB\x97"B\x1d}\xa2m8v\x9a\xcf.:\x9f\xf2\xd9@\x11.\x92\xd0\x1dkHzet\xd7\xe6\xc0j\xab\xad\xff\xb3\xe6$\x97\xfd=\x0b\x1c%_\xd1\xa9"'
m9 = '###Should you use a random nonce with oaep?'
################

################
e10 = 65537
n10 = 98326993759634789515778687799020543645398962489890436310231025647956456166685176265303236823165224008000474960054742885390051491705558213022700710136581245927093740780985394183390749017153700221212481058983678953171251665248666951370742484457781880038452217032906924859256620548427923611534146579043548158531
cipher10 = '?+\xdfn\x17R\xfc;\x84\xcc<)\xceC\xad\x12y\xaa\x85#\xf1G\xd0\x1fF\xd1F\xc4\xdb\x00\xd0\x8c\xc7\xc1\xa0\xc6}P\xd3\xf0\nHB\xdb\x1b\xd3A\xab8\x0f\xcf\xc6\xe9N\x01\x03\x96\n\xb7\x1bU[\xd3\xf2\xe1z\xe2Y\xb0bH\x0f\xd1\x12\x80\xe3\xb7\x1b\x1aU\xd8\xf3\x8c\xcc\xa1\xad\x8dK\xc8\xba\xc4\xcd\x18j"A\xb6\x1b\xd0\xc4\xd5\x9aVT]biR\xb0\xa8p\xc1U$\t\x97\xfe\r(\x95\xc5V\xff]#\xa2\xe3\xf6'
m10 = 'Fermat was a smart guy. He might have some hints on factoring'
################

################
e11 = 65537
n11 = 59271838373237712241010698426785545947980750376894660532845611609385295493574642459966039842508102834600550821189433548722152899983884277266737416092985257305168009937861700509240511070647418413603755912503843488856979904991517729100725512850421664634705274281314737938901139871448406073842088742598680079967
cipher11 = 'J\xc1R\x90\xe1\xf4\x8b5My\xf8\xa1\xf4>\xa2\xc3\x10\xbd\xeb\xcc&\x7fb\x1aC$\x1d\xc5\xb7\xcdz\xb7\x17\x8a#9\x12\x89\xfeao\x19\x9c\xeb\xb0>\x86\x9b\x1d3~b0-u\xfc\x04!\rc\\\xcb$\x91\x9e\xa1N\x9d2\xff\x19\x9a9vH.\xd5\xe7m\xa9m\xea^\xd3T$\xd7\xd7\x11\x81\xe4B\x9b~\x8c $\xa6K\x8a\xdc`\xb4\x9cu\xfb\xc2\x06\xd1\xbb\xb9\xa0\x8f\xd2\xbc\x02\xf6#\x1f\x1dM\xbb\x98\xf2\xa0\x9fO\x80'
m11 = 'What could go wrong: http://pastebin.com/hNz9gZbe'
################

################
e12 = 65537
n12 = 72216220929585874029800250341144628594049328751082632793975238142970345801958594008321557697614607890492208014384711434076624375034575206659803348837757112962991028175041084288364853207245546083862713417245642824765387577331828704441227356582723560291425753389466410790421096831823015438162111864463275922441
cipher12 = ".\xfd9\x8dc\xda\xf9o\xf5Vl\xfb\x87\xed\xd5 \xee\xcf\x97~\xd8T\xf9.\x18\xb1\xd5n^\xa0\rA\xe0\x1d\xd5\xc8:D\xc9\x14o\xde\xdbo\xf9>)bc'a\xa2\x8e\xc1|\xdd\r[q1\xac\x0f^\x82b/A\x10\x87\xff\xe4k=\xc8\xd6\x1c\x7f\xfb\xdb\xda&\xd9\xc5\xc4\x8a#\xa0u\x03J&\n\x83\xa0\xe1.\xba\xfd\x8a0s?\xdeg\xd50\x15\xeb\x91\xb3E\xc7\x15O\xf3r\xe3`~8\xb4\xb5=\x89U\x7f\xfa\x19"
m12 = 'A real example: http://digitaloffense.net/tools/debian-openssl'
################

################
e13 = 3
n13 = 70312356315714780126407430932110548424144037560501611854827137092512910875581601526352040261858471208166388560443445258525272960150598064892138505585965821412085549228607722662540954787033730390722435251172318708904239583536234789288179180688257614871029465697421428231000338910272301520713624044424711448629
cipher13 = '&\xb91\x8ex\x91!0\x855jX\xd1Y\xfc\x9a \xf1\xd9\x9a\xa4\x84s\x0c\xf0\x96\x9e\xcc\xa4L\xe6o\x12\x11~\xd8\xef\x11-t\xf5\xfce\x8a\xb1\xc2mL\xa8\xaa\xb71\xd4y\xa4\xd1\x15\xfdn\x1a\x16\xdf\xfb\xe7\x83Zi\x8f\xb7\x151K\xc72\xf6\xe6\xb31c\xc9\x18\xe9\x92u]\x9f\x01j\x12\xd2\xd3Y("\x9bm9\xc3\x1a9\x1e\xb4\xd4\xa3\xfei\x97\x8a\xa3k\xdc}\xfcy\xf4z\x96\x98\xbev\xce\xa5j\xfdk!xV'
m13 = 'we recommend you read this blog: http://goo.gl/5I1lt'
################

################
e14 = 65537
n14 = 99428965906962816070784007311850456823957258033424536090292194626620222742187661756726403412281396587119713030320975423136670466362256289782688266974070489861007966741029067535118700826392643025215295741522514598507712664582141077802475427001379922637288480239204598457282788664201418160351588075772782828233
cipher14 = ':\xba\xb7\x0f`\x959\xc2\x900\xf0b\xb3\xe6\xde\xe6\x80\xdf\xc9\x1b\xed\xa6G\x90\x0c\xc2\xa4Z\xc1\x85n\xb6K/\x97\xd4\x9b\x0cKC\x1b\x9e\x83\x13{\x8a\xa6\xa3\x01\xed\x142\xf3\xab\xbb\x1f\x96bQO\x00\x1c\xc5\xba\xfc\xaf\xf2=\x9c\xaa\x94&3aN\r\xe2xh\xad\x18\xf4X\xc1;\xe8\xbcmOn]\xd2JO:+z\xbd\xa6_Q\x10\xf8\xde\xf6`\xdfF\xfa<\xe3 N%$ev\x08\xdai\x85\x8f\x17\xfb,\xa9s\x85'
m14 = ''#YOUR ANSWER HERE
################

################
e15 = 65537
n15 = 118399170574854942444633896245235023966560880236530051363584486215325592633889564680653306117442159965072738319247448982717567259059972729844114596818478915558131833772330699563816353891596654144981880987927436049203299944850160662951894970183034856877612682945727163824998131146307156333199771146520933436033
cipher15 = '@\xc4X\x1a\xae\xb6C\x12.\xfcvK\x90s\xbe\xf2\xab\xda#j\xba\xf7\x81\xee\xa2\xb2\xddR~Z\xbak(u\xee\x90\xf9\xbc\xe3m\xc8\xdb\xf37k\xe8\xb0\xac\xc2T\xe9\x97\xe4\x01~\xdd\xd4A\xd3\xe9\\\x876}#\xddK7n\xae\x1e\xed\xe6z\x82Zp\xe5c\xc0C\xbd\xf9\x8bD\x03\x19\x9d\xb5s \x0f\xe1c\xd4\xf5M\xc4\xbc\x971\x87\xd6\xb5\x1d\x10\xb7\xc4/\xf6\x8d!u\xed\xe9|U\xbe\x98\xbaLLp\x8ehZ\xec\x1d'
m15 = ''#YOUR ANSWER HERE
################


from hashlib import sha512

BITS = ('0', '1')
ASCII_BITS = 8
HASH_BITS = 128 * ASCII_BITS // 2

### bits_to_*
def bits_to_char(b):
	assert len(b) <= ASCII_BITS
	value = 0
	for e in b:
		value = (value * 2) + e
	return chr(value)

def bits_to_string(b):
	return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
					for i in range(0, len(b), ASCII_BITS)])

def bits_to_int(b):
	value = 0
	for e in b:
		value = (value * 2) + e
	return value

### string_to_*
def string_to_int(s):
	return bits_to_int(string_to_bits(s))
	
def pad_bits(bits, pad):
	"""pads seq with leading 0s up to length pad"""
	assert len(bits) <= pad
	return [0] * (pad - len(bits)) + bits

def string_to_bits(s):
	def chr_to_bit(c):
		return pad_bits(int_to_bits(ord(c)), ASCII_BITS)
	return [b for group in 
			map(chr_to_bit, s)
			for b in group]

### int_to_*
def int_to_bits(n):
	result = []
	if n == 0:
		return [0]
	while n > 0:
		result = [n % 2] + result
		n = n / 2
	while len(result) % ASCII_BITS != 0:
		result = [0] + result
	return result

def int_to_string(n):
	return bits_to_string(int_to_bits(n))

### other stuff
def cube_root(n):
	lo = 0
	hi = n
	while lo < hi:
		mid = (lo + hi) // 2
		if mid ** 3 < n:
			lo = mid + 1
		else:
			hi = mid
	return lo

def mod_exp(a, b, q):
	### better use: pow(a, b, q)
	"""return a**b % q"""
	val = 1
	mult = a
	while b > 0:
		odd = b & 1 # bitwise and
		if odd == 1:
			val = (val * mult) % q
			b -= 1
		if b == 0:
			break
		mult = (mult * mult) % q
		b = b >> 1 # bitwise divide by 2
	return val

def hash(v):
	h = sha512(bits_to_string(v)).digest()
	return string_to_bits(h)[:HASH_BITS]

def xor(a, b):
	assert len(a) == len(b)
	return [aa^bb for aa, bb in zip(a, b)]

def oaep_pad(message, nonce):
	mm = message + [0] * (HASH_BITS - len(message))
	G = xor(mm, hash(nonce))
	H = xor(nonce, hash(G))
	return G + H
	
def oaep_encode(message, e, n, nonce):
	oaep = oaep_pad(message, nonce)
	m_int = bits_to_int(oaep)
	return pow(m_int, e, n)

def oaep_decode(bits):
	G = bits[:HASH_BITS]
	H = bits[HASH_BITS:]
	assert len(bits) == 2 * HASH_BITS
	assert len(G) == HASH_BITS
	assert len(H) == HASH_BITS
	r = xor(hash(G), H)
	m = xor(G, hash(r))
	return m, r

from string import printable
valid_chars = set(c for c in printable)
valid_chars.add(' ')
def isValid(decode_guess):
	return all(d in valid_chars for d in decode_guess)

# decode the message and while doing that collect nonces
nonce = []
def decode(message, n):
	for i in range(0, 10):
		m = int_to_string(message + i * n).strip('\x00')
		if isValid(m):
			return m
	for i in range(0, 10):
		b = int_to_bits(message + i * n)
		if len(b) == HASH_BITS * 2:
			m, ri = oaep_decode(b)
			m = bits_to_string(m).strip('\x00')
			if isValid(m):
				nonce.append(ri)
				return m
	return None	

from math import sqrt
from itertools import count, islice
#def isPrime(n):
#	if n < 2: return False
#	return all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def isPrime(N):
	 if N == 1:
		 return 0
	 if N in sieve:
		 return 1
	 for i in sieve:
		 if (N % i)==0:
			 return 0
 
	 # Compute the highest bit that's set in N
	 N1 = N - 1
	 n = 1
	 while (n<N):
		 n=n<<1
	 n = n >> 1
 
	 # Rabin-Miller test
	 for c in sieve[:7]:
		 a=long(c) ; d=1 ; t=n
		 while (t):  # Iterate over the bits in N1
			 x=(d*d) % N
			 if x==1 and d!=1 and d!=N1:
				 return 0  # Square root of 1 found
			 if N1 & t:
				 d=(x*a) % N
			 else:
				 d=x
			 t = t >> 1
		 if d!=1:
			 return 0
	 return 1
 
# Small primes used for checking primality; these are all the primes
# less than 256.  This should be enough to eliminate most of the odd
# numbers before needing to do a Rabin-Miller test at all.
 
sieve = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
	61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
	131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
	197, 199, 211, 223, 227, 229, 233, 239, 241, 251]
 	
############################################################################
# cipher1: too short message (m^3 < n)
# cipher9: too short message (n < m^3 < 2n)
############################################################################
def messageTooShortAttack(ex, c, e, n, factor):
	mi = cube_root(c + factor * n)
	assert pow(mi, e, n) == c
	m = decode(mi, n)
	print ex
	print m
	
############################################################################
# cipher 2, 8, 13: chinese remainder theory
############################################################################
def chinese_remainder(n, a):
	sum = 0
	prod = reduce(lambda a, b: a * b, n)

	for n_i, a_i in zip(n, a):
		p = prod / n_i
		sum += a_i * mul_inv(p, n_i) * p
	return sum % prod

def mul_inv(a, b):
	b0 = b
	x0, x1 = 0, 1
	if b == 1: return 1
	while a > 1:
		q = a / b
		a, b = b, a % b
		x0, x1 = x1 - q * x0, x0
	if x1 < 0: x1 += b0
	return x1

def sameMessageAttack(ex, c1, n1, c2, n2, c3, n3):
	mi3 = chinese_remainder([n1, n2, n3], [c1, c2, c3])
	assert pow(mi3, 1, n1) == c1
	assert pow(mi3, 1, n2) == c2
	assert pow(mi3, 1, n3) == c3
	
	n123 = n1 * n2 * n3
	while True:
		mi = cube_root(mi3)
		if mi ** 3 == mi3:
			assert pow(mi, 3, n1) == c1
			assert pow(mi, 3, n2) == c2
			assert pow(mi, 3, n3) == c3
			m = decode(mi, n1)
			print ex
			print m
			return

		mi3 = mi3 + n123
	
############################################################################
# cipher 11, 12: 2 n's sharing same factor p
############################################################################
def calcD(totient, e):
	u0 = 1
	d = 0
	u2 = totient
	v0 = 0
	v1 = 1
	v2 = e
	while v2 != 0:
		q = u2 // v2
		u0, v0 = v0, u0 - q * v0
		d, v1  = v1, d  - q * v1
		u2, v2 = v2, u2 - q * v2

	if d < 0: d += totient
	assert (e * d) % totient == 1
	return d

from fractions import gcd
def sharedFactorAttack(ex, c, e, n, p):
	q = n // p
	totient = (p - 1) * (q - 1) 
	d = calcD(totient, e)
	mi = pow(c, d, n)
	assert pow(mi, e, n) == c
	m = decode(mi, n)
	print ex
	print m
	
############################################################################
# cipher 0, 6: close factors p and q
############################################################################
def isqrt(n):
	x = n
	y = (x + 1) // 2
	while y < x:
		x = y
		y = (x + n // x) // 2
	return x

def fermat(n):
	a = b = isqrt(n)
	b2 = a ** 2 - n
	while b ** 2 != b2:
		a = a + 1
		b2 = a ** 2 - n
		b = isqrt(b2)
	p = a + b
	q = a - b
	assert n == p * q
	return p, q

def closeFactorsAttack(ex, c, e, n):
	p, q = fermat(n)
	if p == None:
		print ex
		print "------"
		return None
	totient = (p - 1) * (q - 1) 
	d = calcD(totient, e)
	mi = pow(c, d, n)
	assert pow(mi, e, n) == c
	m = decode(mi, n)
	print ex
	print m

############################################################################
# cipher 4, 10: low resolution random generator
############################################################################
import random
from Crypto.Util import number
def randfunction(N):
	# N is in bytes
	# pycrypto expects a string
	l = []
	while N > 0:
		l.append(chr(random.getrandbits(8)))
		N -= 1
	return "".join(l)

def badRandomAttack(ex, c, e, n, start = 0):
	if start == 0: print ex
	for i in range(start, 32768):
		if i % 100 == 0: print i
		random.seed(i)
		p = number.getPrime(512, randfunction)
		q = n // p
		if q * p == n:
			if start == 0: print "found at", i
			totient = (p - 1) * (q - 1) 
			d = calcD(totient, e)
			mi = pow(c, d, n)
			assert pow(mi, e, n) == c
			m = decode(mi, n)
			print ex
			print m
			return
		if start != 0:
			print ex
			print "------"
			return

############################################################################
# Sanity checks
############################################################################
def sanityCheck():
	# check string_to_int and vv
	ci = string_to_int(cipher0)
	c = int_to_string(ci)
	assert c == cipher0

	# check int_to_bits and vv
	i = n0
	bi = int_to_bits(i)
	b = bits_to_int(bi)
	assert b == i

	# check rsa
	e = 7
	d = 3
	n = 33
	mi = 2
	ci = pow(mi, e, n)
	mci = pow(ci, d, n)
	assert mci == mi 

	# check mod_exp
	e = 7
	d = 3
	n = 33
	mi = 2
	ci = mod_exp(mi, e, n)
	mci = mod_exp(ci, d, n)
	assert mci == mi 

	# check chinese remainder theory
	assert chinese_remainder([3, 5, 7], [2, 3, 2]) == 23

	# check fermat
	n = 103591 * 104729
	p, q = fermat(n)
	assert p * q == n

	# check cube_root
	cn = cube_root(n0 ** 3)
	assert n0 == cn

############################################################################
# Handy!
############################################################################
c0 = string_to_int(cipher0)
c1 = string_to_int(cipher1)
c2 = string_to_int(cipher2)
c3 = string_to_int(cipher3)
c4 = string_to_int(cipher4)
c5 = string_to_int(cipher5)
c6 = string_to_int(cipher6)
c7 = string_to_int(cipher7)
c8 = string_to_int(cipher8)
c9 = string_to_int(cipher9)
c10 = string_to_int(cipher10)
c11 = string_to_int(cipher11)
c12 = string_to_int(cipher12)
c13 = string_to_int(cipher13)
c14 = string_to_int(cipher14)
c15 = string_to_int(cipher15)

N = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15]
E = [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]
C = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15]
M = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15]
ALL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
SOLVED = [0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13]
UNSOLVED = [3, 5, 7, 14, 15]

############################################################################
# Solve!!
############################################################################
sanityCheck()
p11_12 = gcd(n11, n12)
closeFactorsAttack("exercise 0", c0, e0, n0)
messageTooShortAttack("exercise 1", c1, e1, n1, 0)
sameMessageAttack("exercise 2", c2, n2, c8, n8, c13, n13)
badRandomAttack("exercise 4", c4, e4, n4, 22409)	# does not work at home pc???
closeFactorsAttack("exercise 6", c6, e6, n6)
sameMessageAttack("exercise 8", c2, n2, c8, n8, c13, n13)
messageTooShortAttack("exercise 9", c9, e9, n9, 1)
badRandomAttack("exercise 10", c10, e10, n10, 7026)	# does not work at home pc???
sharedFactorAttack("exercise 11", c11, e11, n11, p11_12)
sharedFactorAttack("exercise 12", c12, e12, n12, p11_12)
sameMessageAttack("exercise 13", c2, n2, c8, n8, c13, n13)

###	############################################################################
###	# Experiment: nonce reused (m9)
###	############################################################################
###	text = []
###	# add the text from T.S. Eliot - text referenced by m0 and m6
###	text.append("We shall not cease from exploration")
###	text.append("And the end of all our exploring")
###	text.append("Will be to arrive where we started")
###	text.append("And know the place for the first time.")
###	text.append("Through the unknown, unremembered gate")
###	text.append("When the last of earth left to discover")
###	text.append("Is that which was the beginning;")
###	text.append("At the source of the longest river")
###	text.append("The voice of the hidden waterfall")
###	text.append("And the children in the apple-tree")
###	text.append("Not known, because not looked for")
###	text.append("But heard, half-heard, in the stillness")
###	text.append("Between two waves of the sea.")
###	text.append("Between two waves of the sea")
###	text.append("Quick now, here, now, always-")
###	text.append("A condition of complete simplicity")
###	text.append("(Costing not less than everything)")
###	text.append("And all shall be well and")
###	text.append("All manner of thing shall be well")
###	text.append("When the tongues of flame are in-folded")
###	text.append("Into the crowned knot of fire")
###	text.append("And the fire and the rose are one.")
###	# and a reference to m4
###	text.append("Over the Wintry. -Natsume Soseki")
###	text.append("What hath God wrought? -Samuel Morse")
###	# add quotes from earlier tasks (most of them are too long)
###	text.append("One if by land; two if by sea")
###	#text.append("Trust, but verify. -a signature phrase of President Ronald Reagan")
###	#text.append("The best way to find out if you can trust somebody is to trust them. (Ernest Hemingway)")
###	#text.append("If you reveal your secrets to the wind, you should not blame the wind for revealing them to the trees. (Khalil Gibran)")
###	#text.append("I am not very good at keeping secrets at all! If you want your secret kept do not tell me! (Miley Cyrus)")
###	text.append("This message is exactly sixty four characters long and no longer")
###	text.append("Where is the ANY key? -Homer Simpson")
###	# add found solutions for the sake of testing the code
###	for i in SOLVED:
###		text.append(M[i])
###	
###	# nonces are added while decoding previous messages (oaep_decode)
###	
###	# nonces from cipher0 & 6
###	#nonceM0 = int_to_bits(1432418676436716208706958119837787028875504791733452125391263822915077665497959764580158692965645332187600515530039557217115603663634143115796464962378503)
###	#nonceM6 = int_to_bits(10241105553738919638754998566336364981175036452437347313032801860397943855958374927348537860656022547468515387776972434785755616718411827661550306822270382)
###	#nonce = [nonceM0, nonceM6]
###	def dictionaryAttack(ex, c, e, n):
###		print ex
###		for i in range(0, len(text)):
###			m = text[i]
###			mi = string_to_int(m)
###			mb = int_to_bits(mi)
###			# first try plain message
###			ci = pow(mi, e, n)
###			if ci == c:
###				print ex
###				print m
###				return m
###			# second try encrypted message with all found nonces
###			for j in range(0, len(nonce)):
###				ci = oaep_encode(mb, e, n, nonce[j])
###				if ci == c:
###					print ex
###					print m
###					return m
###			
###	print
###	print "reused nonce?"
###	for i in UNSOLVED:
###		dictionaryAttack("exercise " + str(i), C[i], E[i], N[i])
###	
###	############################################################################
###	# Experiment: two digits attack
###	############################################################################
###	def fewDigitAttack(ex, c, e, n):
###		print ex
###		for mi in range(10, 10000):
###			mb = int_to_bits(mi)
###			ci = pow(mi, e, n)
###			if ci == c:
###				print mi
###				return
###	
###	print
###	print "few digits?"
###	for i in UNSOLVED:
###		fewDigitAttack("exercise " + str(i), C[i], E[i], N[i])
###	
###	############################################################################
###	# Experiment: message reused
###	############################################################################
###	def reuseMessageAttack(ex, c, e, n):
###		print ex
###		for i in range(0, len(N)):
###			if len(M[i]) == 0: continue
###			m = M[i]
###			mi = string_to_int(m)
###			mb = int_to_bits(mi)
###			# first try plain message
###			ci = pow(mi, e, n)
###			if ci == c: print i
###			# second try encrypted message with all found nonces
###			for j in range(0, len(nonce)):
###				ci = oaep_encode(mb, e, n, nonce[j])
###				if ci == c: print i
###			
###	print
###	print "message reused?"
###	for i in UNSOLVED:
###		reuseMessageAttack("exercise " + str(i), C[i], E[i], N[i])
###	
###	############################################################################
###	# Experiment: cycling
###	############################################################################
###	def xcyclingAttack(ex, c, e, n, start):
###		if start == 0: print ex
###		for i in range(start, 75000):
###			if i % 100 == 0: print i
###			c = pow(c, e, n)
###			m = decode(c, n)
###			if m != None:
###				print ex
###				print m
###				return
###	
###	def ycyclingAttack(ex, c, e, n, start):
###		if start == 0: print ex
###		for i in range(start, 50000):
###			if i % 1000 == 0: print i
###			mi = pow(c, pow(e, i), n)
###			m = decode(mi, n)
###			if m != None:
###				print ex
###				print m
###				return
###	
###	print
###	print "cycling?"
###	for i in UNSOLVED:
###		cyclingAttack("exercise " + str(i), C[i], E[i], N[i], 0)
###	
###	############################################################################
###	# Experiments: Wiener Attack
###	############################################################################
###	from RSAwienerHacker import hack_RSA
###	def wienerAttack(ex, c, e, n):
###		print "exercise", ex
###		d = hack_RSA(e, n)
###		print "d", d
###	
###	print
###	print "wiener?"
###	for i in ALL:
###		wienerAttack("exercise " + str(i), C[i], E[i], N[i])
###
	
############################################################################
# EOF
############################################################################

