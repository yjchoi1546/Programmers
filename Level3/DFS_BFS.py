# 문제 설명
## 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
## 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
## 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
## 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

## 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
## 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#########################################################################################

# 제한사항

## 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
## 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
## i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
## computer[i][i]는 항상 1입니다.

#########################################################################################

# 내 방법

# DFS 방법 -> stack 자료구조 이용(LIFO)
def Solution(n, computers):
    answer = 0
    visited = [False]*n # 컴퓨터 방문 여부
    # 여기서 visited : 방문 여부를 리스트로 표시. *n 은 0부터 n-1 번까지의 컴퓨터까지
    # 방문 여부를 저장. ex ) [False] * 5 = [False, False, False, False, False] 처럼 길이가 n 이고, False로 초기화 된 리스트를 만드는 것.

    for i in range(n):
        if not visited[i]:
            answer += 1 # 새로운 네트워크의 시작점이므로 넷웤 개수 answer 1 증가
            stack = [i] # stack에 현재 컴퓨터 [i] 추가
            visited[i] = True # 현재 컴퓨터 i를 방문했다고 표시 -> 다시 방문하지 않도록 하기위해서.
 
            while stack: # stack 이 비어있지 않는 동안 계속 반복해야지.
                current_computer = stack.pop() # stack의 맨 위 컴퓨터 꺼냄.

                # 현재 컴퓨터와 연결된 다른 모든 컴퓨터 확인
                for next_computer in range(n):
                    if computers[current_computer][next_computer] == 1 and not visited[next_computer]:
                        # current_computer 와 next_computer가 연결 되어있고, next_computer가 아직 방문하지 않았으면,
                        stack.append(next_computer) # 다음 컴퓨터를 스택에 추가
                        visited[next_computer] = True # 그 다음 방문 했다고 처리
    return answer

# 다른 사람 풀이(다음에 알아보자)

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
    








    return answer