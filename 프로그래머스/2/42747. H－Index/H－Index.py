def solution(citations):
    answer = 0

    for h in range(max(citations)+1, 0, -1):
        count = 0
        for c_num in citations:
            if c_num >= h:
                count += 1
        
        if count >= h:
            return h
                
    return 0