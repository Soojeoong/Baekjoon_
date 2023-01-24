# https://www.acmicpc.net/problem/1259
from sys import stdin

def Palindromes(N):
    if N == N[::-1]:
        print('yes')
    else:
        print('no')

while True:
    N = stdin.readline().rstrip()
    if N == "0":
        break
    Palindromes(N)

# N = [1,2,4,2,1]
# N[::-1] = [1,2,4,2,1]
