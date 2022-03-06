# https://techblog-history-younghunjo1.tistory.com/177?category=1014800

# BFS(너비 우선 탐색: Breadth-first search, BFS) = 맹목적 탐색  https://ko.wikipedia.org/wiki/%EB%84%88%EB%B9%84_%EC%9A%B0%EC%84%A0_%ED%83%90%EC%83%89
# 가장 가까운 노드부터 탐색
# 큐라는 자료구조를 활용해서 구현
# FIFO(First-In-First-Out)
# 동일한 깊이의 노드가 여러개 있다면 큐에 노드에 새겨진 숫자가 작은 노드들 부터 삽입
# 나동민 7분 동영상 강의 : https://www.youtube.com/watch?v=l0Rsu7dziws

# BFS - 너비 우선 탐색 - 큐(FIFO)를 이용. collections의 deque 이용!
from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 코드

visited = [False] * len(graph)

def bfs(graph, start, visited):
    # 시작 노드를 큐에다가 먼저 삽입(삽입할 때 파이선 리스트[]로 감싸주기)
    queue = deque([start])
    # 시작 노드를 방문 처리
    visited[start] = True
    
    # 큐에서 노드를 pop하고 그 노드의 인접노드들을 탐색. 단, 큐가 빌(False)때 까지
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
  
bfs(graph, 1, visited)