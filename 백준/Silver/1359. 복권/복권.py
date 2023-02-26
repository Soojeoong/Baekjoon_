import sys
import math

n,m,k = map(int, sys.stdin.readline().split())
#조합으로 
def nCm(n, m):
    if n < m: return 0
    return math.factorial(n) / (math.factorial(n-m) * math.factorial(m))

result = 0
#k개의 경우의 수르 ㄹ고려
for K in range(k,m+1):
    result += (nCm(m,K)*nCm(n-m,m-K)/nCm(n,m))

print(result)