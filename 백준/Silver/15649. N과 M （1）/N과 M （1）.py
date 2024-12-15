def dfs(n, lst): # n : 지금까지 선택한 숫자 개수, lst : 지금까지 선택한 숫자들
    # 종료 조건(n에 관련) + 정답처리
    if n==M: # M개의 수열을 완성
        ans.append(lst)
        return
    
    # 하부단계(함수) 호출
    for j in range(1, N+1):
        if v[j]==0: # 선택하지 않은 숫자인 경우추가
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0

N, M = map(int, input().split())
# M개가 출력 이중리스트인데 (M, N인거)

ans = []  # 정답 리스트를 저장할 리스트
v = [0]*(N+1) # 중복확인을 위한 visited[]

dfs(0, [])
for lst in ans:
    print(*lst) # 리스트를 풀어서 출력