#!/usr/bin/python2

# TODO: write docs

def char2number(c):
    # Some magic contastants from ascii table
    UPPER_MIN = 65
    UPPER_MAX = 90
    LOWER_MIN = 97
    LOWER_MAX = 122
    OFFSET = LOWER_MIN - UPPER_MIN

    n = ord(c)

    capital = False
    # Check if letter is capital
    if n >= UPPER_MIN and n <= UPPER_MAX:
        capital = True
        n += OFFSET

    if n < LOWER_MIN or n > LOWER_MAX:
        raise Exception("You promissed!")

    n -= LOWER_MIN

    return n, capital

def char2braille(c):
    # Please note that last 4 letters are special!
    LETTERS = [
        '100000', '110000', '100100', '100110', '100010',
        '110100', '110110', '110010', '010100', '010110',
        '101000', '111000', '101100', '101110', '101010',
        '111100', '111110', '111010', '011100', '011110',
        '101001', '111001', '010111', '101101', '101111',
        '101011',
    ]
    SPACE = '000000'
    CAPITAL = '000001'

    if c == ' ':
        return SPACE

    number, capital = char2number(c)

    braille = ''
    if capital:
       braille = CAPITAL
    
    braille += LETTERS[number]

    return braille

def solution(s):
    result = ''
    for c in s:
        result += char2braille(c)
    return result

def main():
    print(solution("The quick brown fox jumps over the lazy dog"))

if __name__ == "__main__":
    main()
