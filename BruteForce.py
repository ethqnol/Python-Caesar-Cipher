import string

chars = list(string.ascii_lowercase)

def findChar(char):
    i = 0
    if char[i] != " ":
        while char != chars[i]:
            i += 1
    return i


def bruteForce(encrypted):
    shift = 1
    unencrypted = list()
    for i  in range(25):

        for k in range(len(encrypted)):
            if encrypted[k] == " ":
                unencrypted.append(" ")
            else:
                unencrypt = encrypted[k]
                index = findChar(encrypted[k])
                unencrypt = chars[(index+shift) % 26]
                unencrypted.append(unencrypt)
        word = ''.join(unencrypted)
        shift+= 1
        print(">>>", word, "<<<")
        unencrypted = list()


bruteForce("mjqqt k")
