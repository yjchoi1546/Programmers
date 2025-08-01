# 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# 제한 조건
## x는 -10000000 이상, 10000000 이하인 정수입니다.
## n은 1000 이하인 자연수입니다.

# 내 답
def solution(x, n):
    result = []

    for i in range(1,n+1):
        result.append(x*i)

    return result

# 다른 사람 풀이
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]

print(number_generator(2, 5))