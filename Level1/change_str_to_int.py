# 문제 설명
## 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

# 제한 조건
## s의 길이는 1 이상 5이하입니다.
## s의 맨앞에는 부호(+, -)가 올 수 있습니다.
## s는 부호와 숫자로만 이루어져있습니다.
## s는 "0"으로 시작하지 않습니다.

# 내 답
def solution(s):
    answer = int(s)
    return answer

# 다른 사람 풀이
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result

# 이해는 가는데 굳이 이렇게 길게 풀어야하나? 알고리즘 공부하기엔 좋은듯