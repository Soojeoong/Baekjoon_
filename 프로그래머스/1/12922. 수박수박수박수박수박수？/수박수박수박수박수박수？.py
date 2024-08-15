def solution(n):
    answer = ''
    ch = ['수', '박']
    
    for i in range(n):
        answer += ch[i%2]
    return answer