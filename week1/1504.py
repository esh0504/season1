import math

inf = math.inf
board = []
Dijkstra = []

def init_board(N):

    for i in range(N):
        tmpboard = [inf]*N
        tmpboard[i] = 0
        board.append(tmpboard)

def get_minnode(visited, arr):
    min_value = inf
    min_index = 0
    for i in range(len(arr)):
        if visited[i]:
            continue
        min_value = min(arr[i], min_value)
        if min_value == arr[i]:
            min_index = i
    if min_value == inf:
        return inf
    return min_index


def dijkstra(v):
    visited = [False]*len(board)
    visited[v] = True
    di = board[v]
    
    for _ in range(n):
        min_node = get_minnode(visited, di)
        if min_node == inf:
            return di
        visited[min_node] = True
        for i in range(n):
            di[i] = min(board[min_node][i] + di[min_node], di[i])
    return di


if __name__ == '__main__':
    n, e = map(int,input().split())
    init_board(n)
    for i in range(e):
        v1, v2, c = map(int, input().split())
        board[v1-1][v2-1] = c
        board[v2-1][v1-1] = c

    
    v1, v2 = map(int, input().split())
    Dijkstra_start = dijkstra(0)
    Dijkstra_v1 = dijkstra(v1-1)
    Dijkstra_v2 = dijkstra(v2-1)

    answer = min(Dijkstra_v1[v2-1] + Dijkstra_start[v1-1] + Dijkstra_v2[n-1], Dijkstra_v2[v1-1] + Dijkstra_start[v2-1] + Dijkstra_v1[n-1])

    if v1 == 1 or v2 == n:
        if v1 == 1 and v2 == n:
            answer = Dijkstra_start[n-1]
        elif v1 == 1:
            answer = Dijkstra_start[v2-1] + Dijkstra_v2[n-1]
        else:
            answer = Dijkstra_start[v1-1] + Dijkstra_v1[n-1]

    if answer >= inf:
        answer = -1

    print(answer)