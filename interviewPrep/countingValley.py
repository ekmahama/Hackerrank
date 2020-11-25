from collections import Counter


def countingValleys(steps, path):
    # Write your code here
    stepChange = {'U': 1, 'D': -1}
    ret = 0
    strToNum = []
    for s in path:
        strToNum.append(stepChange[s])

    for i in range(1, steps):
        strToNum[i] += strToNum[i-1]
        if strToNum[i-1] == -1 and strToNum[i] == 0:
            ret += 1

    return ret


def countingValleys_v1(steps, path):
    # path = path.strip()
    prev = 0
    cur = 0
    valCnt = 0
    for c in path:
        if c == 'U':
            cur += 1
        elif c == 'D':
            cur -= 1
        if cur == 0 and prev < 0:
            valCnt += 1

        prev = cur
        print(prev)

    return valCnt


#path = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
path = ['D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D']
steps = len(path)
countingValleys(steps, path)

# countingValleys_v1(steps, path)
