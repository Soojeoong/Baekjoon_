# DFS와 BFS
# https://www.acmicpc.net/problem/1260

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)
    
    return

from collections import deque
def bfs(graph, v, visited):
    queue = deque([v]) 
    visited[v] = True
    
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        
        for i in sorted(graph[q]):  # 작은 인접노드부터 방문
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]  # 1부터 시작하는 노드 번호에 맞추기
visited = [False] * (n + 1)

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1) # 양방향 그래프

#print(graph)
dfs(graph, v, visited)
print()

visited = [False] * (n + 1)
bfs(graph, v, visited)
