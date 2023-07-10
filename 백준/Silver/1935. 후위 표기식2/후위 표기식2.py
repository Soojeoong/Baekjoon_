# https://www.acmicpc.net/problem/1935
# 후위 표기식2
num = int(input()) # 피연산자의 개수
exps = list(input()) # 후위 표기식 # input().split()
operand = [int(input()) for _ in range(num)]
# 빈 스택 생성
stack = []
# operator
operators = {
    '+' : lambda x, y: x+y,
    '-' : lambda x, y: x-y,
    '*' : lambda x, y: x*y,
    '/' : lambda x, y: x/y
}

for i in range(len(exps)):
    if exps[i].isalpha(): # if 'A' <= exps[i] <= 'Z'
        stack.append(operand[ord(exps[i]) - ord('A')])
    elif exps[i] in operators:
        op2 = stack.pop()
        op1 = stack.pop()
        result = operators[exps[i]](op1, op2)
        stack.append(result)

print('{:.2f}'.format(result))