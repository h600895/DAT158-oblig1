from vars import *

lastDict = {}


def last(pattern, alphabet):
    for c in alphabet:
        lastDict[c] = -1
    for i, c in enumerate(pattern):
        lastDict[c] = i



def boyer_moore(text, pattern):
    m = len(pattern)
    i = m - 1
    j = m - 1
    compare = 0
    while i <= len(text) - 1:
        compare += 1
        if pattern[j] == text[i]:

            if j == 0:
                return i, compare
            else:
                i -= 1
                j -= 1
        else:
            i = i + m - min(j, 1 + lastDict[text[i].lower()])
            j = m - 1
    return "Pattern not found!", compare
def run_algo(text, pattern, alphabet):
    last(pattern, alphabet)
    return boyer_moore(removeSymbols(text), pattern)


def printStats(compare, text, string):
    comparePercent = format(compare / len(text), '.4f')

    print(string, comparePercent)

def removeSymbols(text):
    symbols = ",.-1234567890?!"

    for s in symbols:
        text = text.replace(s, "")
    return text

if __name__ == '__main__':
    # Norwegian
    nor_res = run_algo(nor_text, nor_pattern, nor_alphabet)
    # English
    eng_res = run_algo(eng_text, eng_pattern, eng_alphabet)

    printStats(nor_res[1], nor_text, "Norwegian: ")
    printStats(eng_res[1], eng_text, "English: ")

    #print(lastDict)
    #result = boyer_moore(text, pattern)
    #print(result)


