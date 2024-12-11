import random


def cipher(key, line):
    result = ''
    for i in range(len(line)):
        char = line[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    return result

def decipher(key, line):
    result = ''
    for i in range(len(line)):
        char = line[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char
    return result

def encrypt(key, line):
    msg = []
    fMsg = ''
    key = str(key)
    calcKey = int(key[0]) + int(key[1]) + int(key[2])
    if len(str(calcKey)) > 1:
        calcKey = str(calcKey)
        calcKey = int(calcKey[0]) + int(calcKey[1])
    if calcKey * len(line) > 100:
        calcKey = 100 // len(line)
    for char in line:
        msg.append(char)
    for i in range(100):
        if i % int(calcKey) == 0 and msg:
            fMsg += msg[0]
            del msg[0]
        else:
            char = chr(random.randint(32,126))
            fMsg += char
    for i in range(0, len(msg), int(calcKey)):
        fMsg[i] = msg.pop()
    return fMsg

def decrypt(key, line):
    msg = []
    fMsg = ''
    key = str(key)
    calcKey = int(key[0]) + int(key[1]) + int(key[2])
    if len(str(calcKey)) > 1:
        calcKey = str(calcKey)
        calcKey = int(calcKey[0]) + int(calcKey[1])
    if calcKey * len(line) > 100:
        calcKey = 100 // len(line)
    for char in line:
        msg.append(char)
    for i in range(100):
        if i % int(calcKey) == 0 and msg:
            fMsg += msg[0]
            del msg[0]
        else:
            char = chr(random.randint(32, 126))
            fMsg += char
    for i in range(0, len(msg), int(calcKey)):
        fMsg[i] = msg.pop()
    return fMsg

def execute(key, line):
    s1 = cipher(key, line)
    s2 = encrypt(key, s1)
    print(s2)

line = cipher(12, 'Hello World')
print(line)
print(decipher(12, line))