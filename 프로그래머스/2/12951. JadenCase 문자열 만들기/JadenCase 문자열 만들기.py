def solution(s):
    words = s.split(' ') # 공백기준 split => 단어들 분리
    
    for i in range(len(words)):
        words[i] = words[i].capitalize()
        
    answer = ' '.join(words)
    return answer