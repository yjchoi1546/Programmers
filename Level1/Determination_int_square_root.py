# 문제 설명
## 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단.
## n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
## n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성.

# 제한 사항
## n은 1이상, 50000000000000 이하인 양의 정수입니다.

# 내 답
def solution(n):
    sqrt_n = n**0.5

    if sqrt_n == int(sqrt_n):
        x = int(sqrt_n)
        return (x+1)**2
    else:
        return -1
    
# 다른 사람 풀이 -> 내 답이랑 유사한데 이게 더 깔끔
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'