
#1 자릿 수 더하기

#문제 설명:
#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
#예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

#제한사항:
#N의 범위 : 100,000,000 이하의 자연수
    

# 자릿 수 더하기
# 내 답
def solution(n):
    answer = 0
    string_n = str(n)

    for digit in string_n:
        answer += int(digit)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드.
print(solution(123))


# 다른 사람 풀이(재귀구조 사용)

#def sum_digit(number):
#    if number < 10:
#        return number
#
#   return number%10 + sum_digit(number//10) #나머지+몫 사용

