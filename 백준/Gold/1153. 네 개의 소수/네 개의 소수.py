# 네 개의 소수 합 == N
import sys
import math

def get_primes(limit):
    """에라토스테네스의 체로 limit 이하의 모든 소수 구하기"""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False # 0과 1은 소수가 아님
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]: # 소수인 경우
            for j in range(i * i, limit + 1, i): # 제곱 이후부터는 소수X
                sieve[j] = False # 배수 제거  
                
    return [i for i in range(limit + 1) if sieve[i]] # 소수 리스트 반환
    

def fine_four_primes(N):
    """네 개의 소수의 합으로 N 표현"""
    primes = get_primes(N) # N 이하의 모든 소수 리스트
    
    # 첫 번째, 두 번째 소수를 고정하고 나머지 두 개를 찾는다!
    for i in range(len(primes)):
        for j in range(i, len(primes)): # 중복 허용 (같은 소수 사용 가능)
            a, b = primes[i], primes[j]
            remaining = N - (a + b)
            
            # 투 포인터로 남은 두 소수 찾기
            left, right = 0, len(primes) - 1
            while left <= right:
                c, d = primes[left], primes[right]
                if c + d == remaining:
                    print(a, b, c, d)
                    return
                elif c + d < remaining:
                    left += 1
                else:
                    right -= 1
                    
    print(-1)


N = int(sys.stdin.readline().strip())
fine_four_primes(N)
