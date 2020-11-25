from collections import Counter


def repeatedString(s, n):
    a_count = s.count('a')
    print(n // len(s) * a_count + s[0:n % len(s)].count('a'))


s = 'aab'
n = 882787
repeatedString(s, n)
