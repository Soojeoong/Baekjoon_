def bfs(si,sj,ei,ej):
    # 생성
    q = []
    v = [[0]*M for _ in range(N)]

    # q에 데이터 한개 삽입
    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.pop(0)
        # 정답처리/종료처리는 이곳에서..!!
        if (ci,cj)==(ei,ej):
            return v[ei][cj]

        # 네방향 반복처리
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            # 범위내, 미방문, 조건맞으면
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]=='1':
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1

    # 이곳에 왔다는 얘기는 종료지점 못찾은 경우: 이런경우는 없음!!
    return -1

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

ans = bfs(0,0,N-1,M-1)
print(ans)