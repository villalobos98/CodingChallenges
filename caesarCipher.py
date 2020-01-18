#author Isaias Villalobos
# This is only a partial implementation of a ceasar cipher encoder and decoder.
#
def CeasarCipherEncoder(string, shift):
    stringResult = ""

    for i in range(len(string)):
        transformedCharacter = transformCharacterEncode(string[i], shift)
        stringResult += transformedCharacter
    print(stringResult)

def CeasarCipherDecoder(string, shift):
    stringResult = ""
    for i in range(len(string)):
        transformedCharacter = transformCharacterDecode(string[i], shift)
        stringResult += transformedCharacter
    print(stringResult)


def CeasarCipher():
    userIn = input("Would you like to encode or decode message. \n")
    message = input("Enter the message: ")
    shift = int(input("Enter shift amount: "))

    # Encoding if user chooses
    if userIn == 'encode':
        CeasarCipherEncoder(message, shift)

    # Decoding if user chooses
    if userIn == "decode":
        CeasarCipherDecoder(message, shift)

def transformCharacterDecode(char, shift):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    obj = enumerate(alphabet)
    alphabetMap = list(obj)

    newIdx = 0
    for i in range(len(alphabetMap)):
        idx, ch = alphabetMap[i]
        if char == ch:
            newIdx = (idx - shift) % 26
            idx, transformedCharacter = alphabetMap[newIdx]
            return transformedCharacter


def transformCharacterEncode(char, shift):
    alphabet = "abcdefghijklmnopqrstuvwxy"
    obj = enumerate(alphabet)
    alphabetMap = list(obj)

    newIdx = 0
    for i in range(len(alphabetMap)):
        idx, ch = alphabetMap[i]
        if char == ch:
            newIdx = (idx + shift) % 26
            idx, transformedCharacter = alphabetMap[newIdx]
            return transformedCharacter



CeasarCipher()