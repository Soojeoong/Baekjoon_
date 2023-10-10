from collections import deque

def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))   
    
    while len(deq) > 1:
        if deq[0]+deq[-1] > limit:
            deq.pop()
            answer += 1
        else:
            deq.pop()
            deq.popleft()
            answer += 1
    if deq: # 남은 숫자가 있다면
        answer += 1
        
    return answer