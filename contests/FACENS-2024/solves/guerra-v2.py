charMap = {
	"A": "@",
	"S": "$",
	"E": "3",
	"I": "!",
	"O": "0",
	" ": "#"
}

def changeChars(string, rotationN):
	resultChars = []
	for char in string:
		if char in char_map:
			resultChars.append(charMap[char])
		elif 'A' <= char <= 'Z':
			position = (ord(char) - ord('A') + n) % 26
			resultChars.append(chr(ord('A') + pos))
		else:
			resultChars.append(char)
	return "".join(resultChars)


while True:
	rotatioN = int(input())
	if rotatioN == 0:
		break

	string = input()

	if len(s) < 1 or len > 51 or n < 1 or n > 20:
		print("ERROR")
		continue

	result = changeChars(string, rotatioN)
	print(result)