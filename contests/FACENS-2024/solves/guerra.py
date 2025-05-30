DEFAULT_CHARS = ["A", "S", "E", "I", "O", " "]

def changeDefaultChars(s):
    if (s == "A"):
        return "@"
    elif (s == "S"):
        return "$"
    elif (s == "E"):
        return "3"
    elif (s == "I"):
        return "!"
    elif (s == "O"):
        return "0"
    elif (s == " "):
        return "#"

def changeChars(string):
    result = ""
    for char in s:
        if (char in DEFAULT_CHARS):
            result += changeDefaultChars(char)
        elif ('A' <= char <= 'Z'):
            pos = (ord(char) - ord('A') + n) % 26
            result += chr(ord('A') + pos)
        else:
            result += char

    print(result)

while True:
    n = int(input())
    if n == 0:
        exit()

    s = input()
    
    if (len(s) < 1 or len(s) > 51):
        print("ERROR")
    elif (n < 1 or n > 20):
        print("ERROR")
    else:
        changeChars(s)