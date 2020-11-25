from collections import Counter


def sockMerchant(n, ar):
    pair_cnt = Counter(arr)
    res = 0
    for p in pair_cnt.values():
        if p > 1:
            res += p//2

    print(res)


arr = [1, 2, 1, 2, 1, 3, 2]
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(arr)

sockMerchant(n, arr)
