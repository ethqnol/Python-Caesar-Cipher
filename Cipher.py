import string

chars = list(string.ascii_lowercase)

def findChar(char):
    i = 0
    if char[i] != " ":
        while char != chars[i]:
            i += 1
    return i

def encrypt(text, shiftVal):
    encryptedText = list()
    for k in range(len(text)):
        if text[k] == " ":
            encryptedText.append(" ")
        else:
            character = text[k]
            index = findChar(text[k])
            character = chars[(index+shiftVal) % 26]

            encryptedText.append(character)
    final = ''.join(encryptedText)

    print(final)

encrypt("hello", 10234123041023401234321234132412341234123412341231421423234231424123423443)






        





