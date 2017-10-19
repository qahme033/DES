import binascii;
import sys

PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4];
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32];
initPermutation = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7];
expTable = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1];		
s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
s4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
s5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
s6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
s7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
s8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
sbox = [s1,s2,s3,s4,s5,s6,s7,s8]
permutationTable = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
inverseInitPermutation = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]


def hexCharToBitString(char):
	return bin(int(char, 16))[2:].zfill(4)
def hexStringToBitString(hexString):
	return "".join([hexCharToBitString(char) for char in hexString ])
def singleByteStringToHexString(byte):
	return hex(int(byte,2))[-1]
def bitStringToHexString(bitString):
	return "".join([singleByteStringToHexString(bitString[i:i+4]) for i in range(0, len(bitString), 4)])



def circularShift(binString, n):
	shiftedBinString = "";
	for i in range(0,len(binString)):
		shiftedBinString += binString[(i+n)%len(binString)];
	return shiftedBinString;


def genRoundKey1(keyBitString):
	afterPermutedChoiceOne = ""
	for index in PC_1:
		afterPermutedChoiceOne += keyBitString[index-1]
	afterLeftCircularShift = circularShift(afterPermutedChoiceOne, 1);
	afterPermutedChoiceTwo = ""
	for index in PC_2:
		afterPermutedChoiceTwo += afterLeftCircularShift[index-1]
	return afterPermutedChoiceTwo

def genL0R0(plainTextBitString):

	afterInitPermuation = ""
	for index in initPermutation:
		afterInitPermuation += plainTextBitString[index-1]

	leftSide = afterInitPermuation[0:64/2]
	rightSide = afterInitPermuation[64/2 : 64]
	return {"L0": leftSide, "R0": rightSide}

def expandR0(r0BitString):
	afterExp = ""
	for index in expTable:
		afterExp += r0BitString[index-1]
	return afterExp


def xor(bitString1, bitString2):
	xoredString = "";
	for i in range(0,len(bitString1)):
		xoredString += str(int(bitString1[i]) ^ int(bitString2[i]))
	return xoredString

def sboxSubstitution(bitString):
	
	sets = [];
	numSets = (len(bitString)+1)/6;

	for i in range(0,numSets):
		start = i*6
		end = start+6
		sets.append(bitString[start:end])

	permutedParts = []
	permuted = ""

	for i in range(0,len(sets)):
		set = sets[i]
		rowString = set[0] + set[-1]
		colString = set[1:-1]
		row = int("0b" + rowString,2)
		col = int("0b" + colString,2)
		permutedPart =  bin(sbox[i][row][col])[2:].zfill(4)
		permuted += permutedPart
		permutedParts.append(permutedPart)

	answerE = permutedParts
	answerF = permuted
	return {"subbedParts" : permutedParts, "subbed" : permuted}

def permutationP(bitString):
	permutedBinString = ""
	for permutation in permutationTable:
		permutedBinString += bitString[int(permutation)-1]
	return permutedBinString
def switchAndInversePermute(l1,r1):
	swapped = r1+l1;
	c = ""
	for permutation in inverseInitPermutation:
		c += swapped[int(permutation)-1]
	return bitStringToHexString(c);

def padText(plainText):
	l = len(plainText)
	for i in range(l, 8) :
		plainText += plainText[i-l];#appending reverse of message to message for padding
	return plainText

def desRound(plainTextHex, keyHex):
	plainTextBitString = hexStringToBitString(plainTextHex)
	keyBitString = plainTextBitString;
	roundKey1 = genRoundKey1(keyBitString);
	l0R0 = genL0R0(plainTextBitString)
	expandedR0 = expandR0(l0R0["R0"])
	a = xor(expandedR0, roundKey1)
	subs = sboxSubstitution(a)
	permutated = permutationP(subs["subbed"])
	r1 = xor(l0R0["L0"], permutated)
	l1 = l0R0["R0"];
	c = switchAndInversePermute(l1,r1);
	# print "Round Key 1 is ", roundKey1 							
	# print l0R0 													
	# print "After expansion R0 is" , expandedR0					
	# print "A is ", a 											
	# print "The permuted parts are " , subs["subbedParts"] 		
	# print "R0 after going through sbox" , subs["subbed"]		
	# print "P(B) is " , permutated								
	# print "R1 is", r1 
	return c;






def main():
	plainText = raw_input("Please enter a message (max 8 characters) : ")
	if(len(plainText) < 8):
		plainText = padText(plainText);
	elif(len(plainText) > 8):
		print "Too many characters"
		main();
	plainTextHex = plainText.encode("hex")
	keyHex = plainTextHex;
	c = des(plainTextHex, keyHex)
	d = des(c, keyHex)

	print "plain text padded"
	print "plain text hex", plainTextHex									
	print "cypher text hex   ", c 
	print "decrypted hex", d
	print "decrypted plain text", plainTextHex.decode("hex")


main()

