from collections import defaultdict


def minimumBribes(q):
    bribes = 0
    q = [v-1 for v in q]

    for i, v in enumerate(q):
        if v - i > 2:
            print('Too chaotic')
            return
        for j in range(max(v-1, 0), i):
            if q[j] > v:
                bribes += 1
    print(bribes)


arr = [2, 1, 5, 3, 4]
# arr = [2, 5, 1, 3, 4]
# arr = [1, 2, 3, 4, 5]
# arr = [4, 1, 2, 3, 5]
# arr = [1, 2, 5, 3, 7, 8, 6, 4]
print(minimumBribes(arr))
