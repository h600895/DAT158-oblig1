import random
import string
import timeit


# Oppgave 9A


def LCSRec(string1, string2, i, j):
    if i < 0 or j < 0:
        return 0
    if string1[i].lower() == string2[j].lower():
        return 1 + LCSRec(string1, string2, i - 1, j - 1)
    return max(LCSRec(string1, string2, i - 1, j), LCSRec(string1, string2, i, j - 1))


# Oppgave 9B

def LCSDyn(string1, string2, pls1, pls2):
    # pls1,2 kun for at det skal være mulig å kalle begge algoritmene fra en run funksjon
    table = [[0 for _ in range(len(string2)+1)]]
    for i in range(1, len(string1) + 1):
        table.append([0])
        for j in range(1, len(string2)+1):
            if string1[i - 1].lower() == string2[j - 1].lower():
                table[i].append(table[i-1][j-1]+1)
            else:
                table[i].append(max(table[i-1][j], table[i][j-1]))
    return table[-1][-1]


def generate_random_string(stringLen):
    return "".join(random.choice(string.ascii_letters) for _ in range(stringLen))


# Oppgave 9C
def run_algo1(string1, string2, function):
    if function == LCSRec:
        start = timeit.default_timer()
        print(LCSRec(string1, string2, len(string1)-1, len(string2)-1))
        stop = timeit.default_timer()
        print("Recursive")
        print(stop - start)
    else:
        start = timeit.default_timer()
        print(LCSDyn(string1, string2))
        stop = timeit.default_timer()
        print("Dynamic")
        print(stop - start)

def run_algo(string1, string2, index):
    # En funksjon kan kjøre begge algoritmene
    functions = [(LCSRec, "Recursive: "), (LCSDyn, "Dynamic: ")]

    start = timeit.default_timer()
    res = functions[index][0](string1, string2, len(string1) - 1, len(string2) - 1)
    stop = timeit.default_timer()
    time = stop - start
    return functions[index][1], res, time


if __name__ == '__main__':
    LENGTH = 13

    string1 = generate_random_string(LENGTH)
    string2 = generate_random_string(LENGTH)

    for i in range(2):
        res = run_algo(string1, string2, i)

        print(res[0], res[-1])



