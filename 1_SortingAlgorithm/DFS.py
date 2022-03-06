# https://techblog-history-younghunjo1.tistory.com/177?category=1014800

# DFS(깊이 우선 탐색: depth-first search, DFS) = 맹목적 탐색  https://ko.wikipedia.org/wiki/%EA%B9%8A%EC%9D%B4_%EC%9A%B0%EC%84%A0_%ED%83%90%EC%83%89
# 깊은 부분을 우선적으로 탐색
# 스택이라는 자료구조를 활용해서 구현
# FILO(First-In-Last-Out)
# 나동민 동영상 강의 : https://www.youtube.com/watch?v=l0Rsu7dziws


# 노드간 간석 부여 값

# 가장 바깥을 감싸고 있는 리스트의 index 값이 노드 번호를 의미
# 각 요소를 이루고 있는 튜블의 첫 번째 값은 노드를 두 번째 값은 두 노드를 연결하는 간선에 부여된 값을 의미

adjacency_list = [[(1, 7), (2, 5)],[(0, 7), (0, 5)]]

# 0번째 index인 0번 노드는 1번 노드와 간선이 7인 값으로 연결되어 있고 2번 노드와 간선이 5인 값으로 연결

# 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용
# 두 노드간의 연결 여부를 확인' 하는 문제에서는 인접 리스트 방식이 정보를 얻는 속도가 느리다는 단점

# DFS - 깊이 우선 탐색 -> 스텍을 이용. 파이썬에서 리스트는 스택으로 구현되어 있음!

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

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 0번 노드가 없으니 1번 노드부터 탐색
dfs(graph, 1, visited)