#자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

#제한 조건
#n은 10,000,000,000이하인 자연수입니다.

# 내 답 -> List comprehension 사용
def solution(n):
    return [int(d) for d in str(n)[::-1]]

# 다른 사람 풀이
# def digit_reverse(n):
#    return list(map(int, reversed(str(n))))