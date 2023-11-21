def Encode(rawData):
    result = ""
    for c in str(rawData):
        result += chr(ord(c) + 10)
        result += chr(ord(c) + 3)
        result += chr(ord(c) + 6)

    return result


def Decode(encoded):
    result = ""

    for i in range(0, len(encoded), 3):
        result += chr(ord(encoded[i]) - 10)

    return result



encoded = Encode(str(input()))
print(encoded)
decoded = Decode(encoded)
print(decoded)
