"""
Simple Affine Cipher
Given parameter a, value given to find modular inverse
Given parameter b, shift amount
Given parameter string, a string to decrypt
"""
def affineCipherDecryption(a, b, string):
    resultString = []
    a_inverse = inverse(a, 26)
    print(a_inverse)
    for y in string:
        # x is the plaintext ascii number, should be converted to ASCII character
        x = a_inverse * (ord(y) - b) % 26 + ord('a')+1
        charValue = chr(x)
        if charValue == 'a':
            charValue -= 98
            resultString.append(charValue)

        resultString.append(charValue)

    print("".join(resultString))

def inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return 1


if __name__ == '__main__':
    string = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
    print(inverse(5, 11))
    # affineCipherDecryption(7, 22, string)
