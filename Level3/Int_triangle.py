# 문제설명
## 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 
## 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 
## 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 
## 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

## 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

# 제한사항
## 삼각형의 높이는 1 이상 500 이하입니다.
## 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

# 내 답
# 아래 -> 위층으로 이동
def solution(triangle):
    
    layer = len(triangle) - 1 # N층의 인덱스

    while layer > 0:
        for i in range(layer): # N번 째 인덱스에는 0부터N -> N+1 개의 숫자 존재.
            # 바로 위층의 칸에 아래칸의 값 두 개 중에서 큰 값 더함.
            triangle[layer-1][i] += max(triangle[layer][i], triangle[layer][i+1])
        layer -= 1 # 위층으로 올라가기

    return triangle[0][0]

# 다른 사람 풀이 1 -> ? 가독성 안좋은데 흠 이건 못짤듯 싶다.
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

# 다른 사람 풀이 2 -> 위층 -> 아래층 방식
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])