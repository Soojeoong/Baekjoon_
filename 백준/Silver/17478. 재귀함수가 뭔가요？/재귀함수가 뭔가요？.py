def chatbot(n, num=0):  # n : 재귀 횟수, num : 들여쓰기 횟수
    tmp = "____" * num  # 들여쓰기
    
    print(tmp + '"재귀함수가 뭔가요?"')
    
    if n == 0:
        print(tmp + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(tmp + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(tmp + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(tmp + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        
        chatbot(n - 1, num + 1)  # n=n-1, num=num+1
    
    print(tmp + "라고 답변하였지.")

N = int(input())  # 재귀 횟수 입력
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
chatbot(N)
