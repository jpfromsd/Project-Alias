# BASIC Interpreter
import sys
from struct import calcsize
import time
import os
import random

token = ''
variables = {}
aName = ''
tracer = False
cCode = 0
aValues = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: ' '
}
endCheck = False
sd = ['⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⡀⢀⠀⢠⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⢠⢤⣀⠀⠀⠀⠈⣆⢧⠈⡆⢸⠀⠀⠀⢰⢡⠇⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀','⠀⠀⠀⢀⠀⠀⣯⢀⣨⠃⠀⠀⠀⠸⡜⣄⣣⢸⠀⠀⠀⡜⡌⠀⠀⠀⠀⢀⡜⡁⠀⠀⠀⠀⠀',
'⠀⠀⠙⢮⡳⢄⠈⠁⠀⢠⠴⠍⣛⣚⣣⢳⢽⡀⣏⣲⣀⢧⡥⠤⠶⢤⣠⢎⠜⠁⠀⠀⠀⠀⠀','⠀⠠⣀⠀⠙⢦⡑⢄⢀⣾⣧⡎⠁⠀⠙⡎⡇⡇⡇⠹⢪⣀⡓⣦⢀⣼⣵⠋⢀⠴⣊⠔⠁⠀⠀','⠀⠀⠈⠑⢦⣀⠙⣲⣝⢭⡚⠃⠀⠀⠀⠸⠸⣹⠁⠀⠀⠀⠉⣹⣪⣎⡸⢞⡵⠊⠁⣀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠈⣷⢯⣨⠷⣝⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠵⣪⢶⣙⡤⠖⢉⣀⠤⠖⠂','⠀⠀⠀⠀⠀⢀⡞⢠⠾⠓⢮⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢬⣺⡯⢕⢲⠉⣥⣀⡀⠀⠀','⠀⠀⢀⡤⣀⢈⡷⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠘⠀⢱⢾⠘⢇⢴⠁⠀⠀',
'⠀⠀⢻⣀⡼⢘⣧⢀⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢙⣞⠆⠀⠀⠀⠀⠀','⠀⠀⠀⠉⠀⢿⡀⠈⠧⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⣹⣦⠇⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠸⢤⡴⢺⡧⣴⡶⢗⡣⠀⡀⠀⠀⠀⡄⠀⢀⣄⠢⣔⡞⣤⠦⡇⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⣀⡤⣖⣯⡗⣪⢽⡻⣅⠀⣜⡜⠀⠀⠀⠸⡜⡌⣮⡣⡙⢗⢏⡽⠁⠰⡏⠙⡆⠀⠀','⠀⠀⣒⡭⠖⣋⡥⣞⣿⡚⠉⠉⢉⢟⣞⣀⣀⣀⠐⢦⢵⠹⡍⢳⡝⢮⡷⢝⢦⡀⠉⠙⠁⠀⠀','⠐⠊⢡⠴⠚⠕⠋⠹⣍⡉⠹⢧⢫⢯⣀⣄⣀⠈⣹⢯⣀⣧⢹⡉⠙⢦⠙⣄⠑⢌⠲⣄⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠘⠧⡴⣳⣃⣸⠦⠴⠖⢾⣥⠞⠛⠘⣆⢳⡀⠈⠳⡈⠳⡄⠁⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⡱⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢣⠀⠀⠉⠀⠈⠂⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⢀⠞⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀',
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀']
sContents = {}
bMode = False
aList = {
    'zed': 722,
    'athena': 643,
    'bartholomew': 231,
    'caustic': 825,
    'gallows': 589,
    'omori': 746,
    'seal': 420
}
caesar = 0


def execute(line):
    try:
        line = [c for c in line]
        scan(line)
        if tracer:
            if token == 'SUNRISE':
                line = ''.join(line).strip()
                sunriseConsole(line)
            elif token == 'SUNSET':
                line = ''.join(line).strip()
                sunsetConsole(line)
            elif token == 'PRINT':
                printStatement(line)
            elif token == 'LET':
                letStatement(line)
            elif token == 'IF':
                ifStatement(line)
        else:
            if token == 'PRINT':
                printStatement(line)
            elif token == 'LET':
                letStatement(line)
            elif token == 'IF':
                ifStatement(line)
    except:
        print('Execution failed')

def printStatement(line):
    line = [c for c in ''.join(line).strip()]
    scan(line)
    args = ','.join(''.join(line).split(',')[1:])
    if type(token) == str and token[0] == '"':
        print(token[1:-1], end ='')
        scan(line)
    else:
        line = [c for c in ''.join(line).replace(' ','')]
        print(calc(line), end='')
    if token == ',':
        printStatement(args)
    else:
        print()

def letStatement(line):
    line = ''.join(line).replace(' ', '')
    if '=' not in line:
        print('Missing assignment operator "="')
        raise ValueError
    name = line.split('=')[0]
    val = line.split('=')[1]
    if val == '':
        print('Missing variable value')
        raise ValueError
    elif val == 'INPUT':
        try:
            print('What value should "' + name + '" be: ')
            value = int(input())
            variables[name] = value
            if name in aList and aList[name] == value:
                global cCode, aName
                cCode = value
                aName = name
                aliasConsole()
        except:
            print('Input must be an integer')
            raise ValueError
    else:
        val = [c for c in val]
        scan(val)
        variables[name] = calc(val)

def ifStatement(line):
    line = ''.join(line).split('THEN')
    if len(line) != 2:
        print('Missing "THEN" in statement.')
        raise ValueError
    line[0] = [c for c in ''.join(line[0]).replace(' ', '')]
    line[1] = [c for c in ''.join(line[1]).strip()]
    line = line[0] + line[1]
    scan(line)
    leftExpr = calc(line)
    op = token
    scan(line)
    rightExpr = calc(line)
    scan(line)
    condition = False
    if op == '>':
        condition = leftExpr > rightExpr
    if op == '<':
        condition = leftExpr < rightExpr
    if op == '>=':
        condition = leftExpr >= rightExpr
    if op == '<=':
        condition = leftExpr <= rightExpr
    if op == '!=':
        condition = leftExpr != rightExpr
    if op == '=':
        condition = leftExpr == rightExpr
    if condition == True:
        execute(token + ' ' + ''.join(line))

def calc(line):
    try:
        result = expression(line)
        if result is not None:
            return result
        else:
            print(f"Please enter a valid expression")
    except:
        print(f"Execution failed. Please try again.")

def expression(line):
    a = term(line)
    while True:
        if token == '+':
            scan(line)
            b = term(line)
            a = a + b
        elif token == '-':
            scan(line)
            b = term(line)
            a = a - b
        else:
            return a

def term(line):
    a = factor(line)
    while True:
        scan(line)
        if token == '*':
            scan(line)
            b = factor(line)
            a = a * b
        elif token == '/':
            scan(line)
            b = factor(line)
            a = int(a / b)
        elif token == '%':
            scan(line)
            b = factor(line)
            a = a % b
        else:
            return a

def factor(line):
    if type(token) == int:
        return token
    if token == '(':
        scan(line)
        a = expression(line)
        if a == None:
            return None
        if token == ')':
            return a
        else:
            return None
    elif token == '-':
        scan(line)
        return -factor(line)
    else:
        return None

def aliasConsole():
    print('The program has encountered an unexpected error.')
    global tracer, bMode
    tracer = True
    flag = input('Please "EXIT" or try again.\n')
    if flag == 'tequila':
        bMode = True
    elif flag == 'EXIT':
        sys.exit()
    else:
        print('Command not recognized. Please try again.')

def sunriseConsole(line):
    line = sunConsole(line)
    eLine = input('Enter line: ')
    splitLine = eLine.split()
    cLines = []
    for split in splitLine:
        cLines.append(cCipher(caesar, split))
    key = aList[aName]
    for c in cLines:
        print(encrypt(key, len(c), c))
    print('Key: ' + str(caesar))

def sunsetConsole(line):
    line = sunConsole(line)
    cLine = input('Enter line: ')
    key = aList[aName]
    eLine = decrypt(key, cLine)
    print(cDecipher(caesar, eLine))

def sunConsole(line):
    global caesar
    cipher = len(line)
    try:
        line = [c for c in line]
        scan(line)
        if token == 'PRINT':
            caesar = 7 * cipher
            printStatement(line)
        elif token == 'LET':
            caesar = 11 * cipher
            letStatement(line)
        elif token == 'IF':
            caesar = 13 * cipher
            ifStatement(line)
    except:
        print('This message will self destruct in five seconds.')
        time.sleep(5)
        selfdestruct()
        sys.exit()

def cCipher(key, line):
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

def cDecipher(key, line):
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

def encrypt(key, key2, line):
    msg = []
    fMsg = ''
    key = str(key)
    key2 = str(key2)
    key2Length  = len(key2)
    calcKey = int(key[0]) + int(key[1]) + int(key[2])
    if len(str(calcKey)) > 1:
        calcKey = str(calcKey)
        calcKey = int(calcKey[0]) + int(calcKey[1])
    for char in line:
        msg.append(char)
    for i in range(100):
        if i % int(calcKey) == 0 and msg:
            fMsg += msg[0]
            del msg[0]
        elif i == (100-key2Length):
            fMsg += key2
        else:
            char = chr(random.randint(32,126))
            fMsg += char
    for i in range(0, len(msg), int(calcKey)):
        fMsg[i] = msg.pop()
    return fMsg

def decrypt(key, line):
    msg = ''
    key = str(key)
    key2 = line[99]
    calcKey = int(key[0]) + int(key[1]) + int(key[2])
    if len(str(calcKey)) > 1:
        calcKey = str(calcKey)
        calcKey = int(calcKey[0]) + int(calcKey[1])
    for i in range((int(key2)*calcKey)):
        if i % int(calcKey) == 0:
            msg += line[i]
    return msg

def aliasWelcome(name):
    print('There is no prize to perfection. Only an end to pursuit.')
    print('Welcome Agent ' + aName.capitalize())
    flag = input('Encrypt or Decrypt?\n')
    if flag == 'encrypt' or 'decrypt':
        try:
            cipherFile = input('Please input the name of the cipher file: ')
            fileOne = open(cipherFile)
            fileOneContents = fileOne.readlines()
            fileOne.close()
            plainFile = input('Please input the name of the file to be ' + flag + 'ed: ')
            fileTwo = open(plainFile)
            fileTwoContents = fileTwo.readlines()
            fileTwo.close()
            if flag == 'encrypt':
                aliasEncrypt(fileOneContents, fileTwoContents)
            elif flag == 'decrypt':
                aliasDecrypt(fileOneContents, fileTwoContents)
            else:
                print('That which inspires us to our greatest good, is also the cause of our greatest evil.')
                print('This message will self destruct in five seconds.')
                time.sleep(5)
                selfdestruct()
                sys.exit()
        except:
            print('Possibility of being compromised. Recommend seeking shelter.')
            selfdestruct()
            sys.exit()
    else:
        selfdestruct()
        sys.exit()

def aliasEncrypt(fileOneContents, fileTwoContents):
    eFileName = ''
    keySet = []
    index = 0
    cLines = []
    for i in range (10):
        char = chr(random.randint(65, 90))
        eFileName += char
    eFile = open(f'{eFileName}.txt', 'a')
    for line in fileOneContents:
        sunConsole(line)
        keySet.append(caesar)
    for line in fileTwoContents:
        words = line.split()
        for word in words:
            cLines.append(cCipher(keySet[index], word))
        index += 1
    for c in cLines:
        key2 = len(c)
        eLine = encrypt(aList[aName], key2, c)
        eFile.write(eLine + '\n')

def aliasDecrypt(fileOneContents, fileTwoContents):
    eFileName = ''
    index = 0
    dLines = []
    msg = ''
    for i in range(10):
        char = chr(random.randint(97, 122))
        eFileName += char
    eFile = open(f'{eFileName}.txt', 'a')
    for line in fileOneContents:
        sunConsole(line)
    for line in fileTwoContents:
        dLine = decrypt(aList[aName], line)
        dLines.append(dLine)
    for d in dLines:
        eFile.write(cDecipher(caesar, d))
        eFile.write(' ')

def selfdestruct():
    for line in sd:
        time.sleep(0.1)
        print(line)

def number(line):
    num = 0
    tok = ''
    while len(line) and line[0].isdigit():
        tok += line[0]
        del line[0]
        num = int(tok)
    return num

def variable(line):
    name = ''
    while len(line) and line[0].islower():
        name += line[0]
        del line[0]
    if name not in variables:
        print('Variable "' + name + '" has not been defined.')
    try:
        return int(variables[name])
    except:
        return int(variables[variables[name]])

def statement(line):
    keyword = ''
    while len(line) and line[0].isupper():
        keyword += line[0]
        del line[0]
    if keyword not in ['PRINT', 'LET', 'IF', 'THEN', 'GOTO', 'SUNRISE', 'SUNSET']:
        print('Unknown keyword: ' + keyword)
        raise ValueError
    else:
        return keyword

def operator(line):
    if line[0] in '<>!' and line[1] == '=':
        op = line[0] + line[1]
        del line[0]
        del line[0]
        return op
    else:
        op = line[0]
        del line[0]
        return op

def string(line):
    msg = ''
    del line[0]
    while len(line) and line[0] != '"':
        msg += line[0]
        del line[0]
    if not len(line):
        print(f'Missing closing "')
        raise ValueError
    else:
        del line[0]
        return '"' + msg + '"'

def scan(line):
    global token
    if len(line) and  line[0].isdigit():
        token = number(line)
    elif len(line) and line[0].islower():
        token = variable(line)
    elif len(line) and line[0].isupper():
        token = statement(line)
    elif len(line) and line[0] in '+-*/%()=<>,':
        token = operator(line)
    elif len(line) and line[0] == '"':
        token = string(line)

def start():
    global endCheck
    print("Welcome to JP's BASIC interpreter! Please enter a command or type EXIT to end")
    while not endCheck and not bMode:
        line = input()
        if line == 'EXIT':

            endCheck = True
        else:
            execute(line)
        if line == 'sd' and tracer:
            selfdestruct()
    while not endCheck and bMode:
        aliasWelcome(aName)
start()
