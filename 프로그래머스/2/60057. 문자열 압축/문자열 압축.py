def solution(s):
    if len(s) == 1:
        return 1
    result = len(s) # 최대 길이는 문자열 길이
    
    # 1~len(s)//2개 단위로 압축
    for i in range(1, len(s)//2+1):
        string = "" # 압축된 문자열 저장
        unit = s[0:i] # 첫번째 단위
        count = 1
        
        # 단위끼리 비교
        for j in range(i, len(s), i):
            # 같으면 계속 count
            if unit == s[j:j+i]:
                count += 1
            # 다르면 count 끊고 string에 추가
            else:
                if count > 1:
                    string += str(count) + unit
                else:
                    string += unit
                # 다음 단위로 넘어가기
                unit = s[j:j+i] # unit 갱신
                count = 1 # count 초기화
        
        # 마지막 단위 추가
        if count > 1:
            string += str(count) + unit
        else:
            string += unit      
        # 최소값 길이 갱신
        result = min(result, len(string))
        
    return result        
