#!/bin/sh
###
### challenge 1
###	decode 2 different messages containing english text encoded with the same key
###

# 1 - make separate words
# 2 - remove unneeded chars
# 3 - sort unique
# 4 - sort on length
if [ $# -ne 0 ] ; then
	sed 's: :\n:g' $@ |
	tr "[A-Z]" "[a-z]" |
	awk '{printf("%d %s\n", length($0), $0);}' |
	sort -u |
	sort -n |
	cut -d " " -f2
else
	cat
fi |
awk '
###
### init
###
BEGIN {
	MIN_LENGTH = 5;

	C1 = "1010110010011110011111101110011001101100111010001111011101101011101000110010011000000101001110111010010111100100111101001010000011000001010001001001010000000010101001000011100100010011011011011011010111010011000101010111111110010011010111001001010101110001111101010000001011110100000000010010111001111010110000001101010010110101100010011111111011101101001011111001101111101111000100100001000111101111011011001011110011000100011111100001000101111000011101110101110010010100010111101111110011011011001101110111011101100110010100010001100011001010100110001000111100011011001000010101100001110011000000001110001011101111010100101110101000100100010111011000001111001110000011111111111110010111111000011011001010010011100011100001011001101110110001011101011101111110100001111011011000110001011111111101110110101101101001011110110010111101000111011001111";

	C2 = "1011110110100110000001101000010111001000110010000110110001101001111101010000101000110100111010000010011001100100111001101010001001010001000011011001010100001100111011010011111100100101000001001001011001110010010100101011111010001110010010101111110001100010100001110000110001111111001000100001001010100011100100001101010101111000100001111101111110111001000101111111101011001010000100100000001011001001010000101001110101110100001111100001011101100100011000110111110001000100010111110110111010010010011101011111111001011011001010010110100100011001010110110001001000100011011001110111010010010010110100110100000111100001111101111010011000100100110011111011001010101000100000011111010010110111001100011100001111100100110010010001111010111011110110001000111101010110101001110111001110111010011111111010100111000100111001011000111101111101100111011001111";
	
	BITS = 7;
		
	ASCII = "";
	for (i = 0; i < 2 ** BITS; ++i) ASCII = ASCII sprintf("%c", i);

	verify();
}

###
### 1000001 --> A
###
function bits2character(bits, ____, i, integer)
{
	integer = 0;
	for (i = 1; i <= BITS; ++i) {
		integer *= 2;
		if (substr(bits, i, 1) == "1") {
			++integer;
		}
	}
	if (integer >= 32 && integer <= 126) {
		return sprintf("%c", integer);
	} else {
		return "#";
	}
}

###
### 10000011000011 --> AB
###
function bits2string(bits, ____, i, string)
{
	string = "";
	for (i = 1; i <= length(bits); i += BITS) {
		string = string bits2character(substr(bits, i, BITS));
	}
	return string;
}

###
### A --> 1000001
###
function character2bits(character, ____, i, bits, integer)
{
	bits = "";
	integer = index(ASCII, character) - 1;
	for (i = 2 ** (BITS - 1); i >= 1; i /= 2) {
		if (integer >= i) {
			bits = bits "1";
			integer -= i;
		} else {
			bits = bits "0";
		}
	}
	return bits;
}

###
### AB --> 10000011000011
###
function string2bits(string, ____, i, bits)
{
	bits = "";
	for (i = 1; i <= length(string); ++i) {
		bits = bits character2bits(substr(string, i, 1));
	}
	return bits;
}

###
### 10000011000011, 11111111111111 --> 01111100111100
###
function exor(string1, string2, ____, i, string)
{
	string = "";
	for (i = 1; i <= length(string1); ++i) {
		if (substr(string1, i, 1) == substr(string2, i, 1)) string = string "0"; else string = string "1";
	}
	return string;
}

###
### sense
###
function sense(string, ____, i, character)
{
	for (i = 1; i <= length(string); ++i) {
		character = substr(string, i, 1);
		if (character >= "0" && character <= "9") continue;
		if (character >= "a" && character <= "z") continue;
		if (character >= "A" && character <= "Z") continue;
		if (character == " ") continue;
		if (character == ",") continue;
		if (character == ".") continue;
		if (character == "!") continue;
		if (character == "?") continue;
		
		return 0;
	}
	return 1;
}

###
### verify
###
function verify(____, key, plaintext, crypttext, backagain)
{
	key =       string2bits("qweasdzxc123456 789poilkjmn");
	plaintext = string2bits("ABCdefGHIjklMNO pqrSTUvwxYZ");
	crypttext = exor(plaintext, key);
	if (plaintext == crypttext) {
		printf("Something is really wrong!!!\n");
		exit;
	}
	backagain = exor(crypttext, key);
	if (plaintext != backagain) {
		printf("Something is really wrong!!!\n");
		exit;
	}
#	printf("%s\n", bits2string(plaintext));
#	printf("%s\n", bits2string(backagain));

	if (length(C1) != length(C2)) {
		printf("lengths not equal!! %d vs %d\n", length(C1), length(C1));
	}
	if (length(C1) % BITS != 0) {
		printf("length %d not multiple of %d bits!!\n", length(C1), BITS);
	}
}

###
### check
###
function check(message, ____, lword, search, lsearch, i, key, plaintext, decoded)
{
	lmessage = length(message);
	search = string2bits(message);
	lsearch = length(search);
	for (i = 1; i <= length(C1) - lsearch + 1; i += BITS) {
		# calculate the key as if at the given position the message to search for is found
		key = exor(substr(C1, i, lsearch), search);
	
		# with that key decode the other message
		plaintext = exor(substr(C2, i, lsearch), key);
		decoded = bits2string(plaintext);

		# and see if it makes sense
#		if (sense(decoded) == 1) {
			printf("%3d: |%s| --> |%s|\n", i / BITS, message, decoded);
#		}
	}
}

###
### every line from the input
###
{
	message = $0;
#	if (length(message) < MIN_LENGTH) {
#		next;
#	}

#	for (i = 97; i <= 122; ++i) {
#		check(message sprintf("%c", i));
#	}
#	check(message ".");
#	check(message ",");
#	check(message " ");
	check(message);
}
'

