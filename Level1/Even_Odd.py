#문제 설명
##정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

#제한 조건
##num은 int 범위의 정수입니다.
##0은 짝수입니다.

# 내 답
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

# 다른 사람 풀이

def evenOrOdd(num):
    #함수를 완성하세요
    if num%2:
        return "Odd"

    return "Even"