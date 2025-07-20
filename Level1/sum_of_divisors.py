# 문제 설명
## 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수
## solution을 완성해주세요.

# 제한 사항
## n은 0 이상 3000이하인 정수입니다.

# 내 답 -> append 함수 활용하려고 이렇게 짠건데 너무 멍청하게 길게품.
def solution(n):
    answer = []

    for i in range(1,n+1):
        if (n % i) == 0:
            answer.append(i)

    return sum(answer)


# 다른 사람 풀이
def solution(n):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])

