from vars import *

def KMP(pattern, text):
    lenPattern = len(pattern) #lenPattern
    lenText = len(text) #lenText

    j = 0
    i = 0

    compare = 0
    found = False
    ff = KMPFailureFunction(pattern)

    while (lenText - i) >= (lenPattern - j):
        compare += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == lenPattern:
            #return f"Fant mønsteret på index {i - j}", compare
            #print("Found pattern at index " + str(i - j))
            found = True
            j = ff[j - 1]

        elif i < lenText and pattern[j] != text[i]:

            if j != 0:
                j = ff[j - 1]
            else:
                i += 1
    if found:
        return "Found pattern at index " + str(i - j), compare
    return "Fant ikke mønstret i teksten", compare

def KMPFailureFunction(pattern):
    ff = [-1] # First index should have value: -1
    lenPattern = len(pattern)
    for i in range(lenPattern):
        j = i

        while True:
            # string.
            if j == 0:
                ff.append(0)
                break
            if pattern[ff[j]] == pattern[i]:
                ff.append(ff[j] + 1)
                break

            j = ff[j]

    return ff

def run_algo(text, pattern):
    KMPFailureFunction(pattern)
    return KMP(pattern, removeSymbols(text))


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
    nor_res = run_algo(nor_text, nor_pattern)
    # English
    eng_res = run_algo(eng_text, eng_pattern)

    printStats(nor_res[1], nor_text, "Norwegian: ")
    printStats(eng_res[1], eng_text, "English: ")



