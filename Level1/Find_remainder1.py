# 문제 설명
## 자연수 n이 매개변수로 주어집니다. 
## n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 
## 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
## 3 ≤ n ≤ 1,000,000

#내 답
def solution(n):
    for i in range(1,n):
        if n%i == 1:
            answer = i
            break

    return answer

# 다른 사람 풀이

def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]

# 다른 사람 풀이2

def solution(n):
    return next(i for i in range(2, n) if n%i == 1)

