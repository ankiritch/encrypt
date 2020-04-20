
class encrypt:
    def __init__(self, msg=" ", key=" "):
        import operator

        numberedAlphabet = {" ": 0,
                        "a": 1,
                        "b": 2,
                        "c": 3,
                        "d": 4,
                        "e": 5,
                        "f": 6,
                        "g": 7,
                        "h": 8,
                        "i": 9,
                        "j": 10,
                        "k": 11,
                        "l": 12,
                        "m": 13,
                        "n": 14,
                        "o": 15,
                        "p": 16,
                        "q": 17,
                        "r": 18,
                        "s": 19,
                        "t": 20,
                        "u": 21,
                        "v": 22,
                        "w": 23,
                        "x": 24,
                        "y": 25,
                        "z": 26,
                        ".": 27,
                        ",": 28,
                        ":": 29,
                        "!": 30,
                        "?": 31}

        numMsg = list()
        newKey = list()
        encryptedNumMsg = list()
        encryptedMsg = ""
        reversedNumAlphabet = {}

        if not msg:
            msg = input("Enter a message that only contains letters and spaces to encrypt or decrypt with XOR: ")

        if not key:
            key = input("Enter a key that only contains letters and spaces to encrypt or decrypt your message with XOR: ")

        msg = msg.lower()
        key = key.lower()
        keyNum = len(key)

        for i in numberedAlphabet:
            newDictKey = numberedAlphabet[i]
            reversedNumAlphabet[newDictKey] = i

        for letter in key:
            newKey.append(int(numberedAlphabet[letter]))


        for letter in msg:
            numMsg.append(int(numberedAlphabet[letter]))

        for number in numMsg:

            if keyNum == len(newKey):
                keyNum = keyNum -1

            if keyNum == len(newKey):
                keyNum = len(key)


        encryptedNumMsg.append(operator.xor(number, newKey[keyNum]))
        print(newKey[keyNum])



        print(encryptedNumMsg)

        for i in encryptedNumMsg:
            encryptedMsg = encryptedMsg + reversedNumAlphabet[i]


        print("Your encrypted/decrypted message with key'", key, "' is: ", encryptedMsg)
        input("")
