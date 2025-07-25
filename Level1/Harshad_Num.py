# 문제 설명
## 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
## 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
## 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수
## solution을 완성해주세요.

# 제한 조건
## x는 1 이상, 10000 이하인 정수입니다.

# 내 답(map 함수 활용) map(int,str) : 문자열의 각 문자를 정수로 변환
# map(function, iterable) : fun -> 각 요소에 적용할 함수, iter -> 함수를 적용할 데이터 집합
def solution(x):
    answer = sum(map(int, str(x)))
    return x % answer == 0

# 다른 사람 풀이
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0