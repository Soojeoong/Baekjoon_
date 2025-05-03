def solution(arr):
    answer = []
    
    num = arr[0] # 가리키는 포인터(비교 대상) 하나 냅두고
    answer.append(num)
    for a in arr:
        if a != num: # 다른게 나오면
            num = a # 포인터 바꾸기
            answer.append(num)
              
    return answer