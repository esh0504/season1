import sys
from collections import deque

def init_board(n):
    board = []
    for _ in range(n):
        lst = list(map(int,sys.stdin.readline().split()))
        board.append(lst)
    return board

def check_boundary(n, m, curr_pos):
    if n <= curr_pos[0] or curr_pos[0] < 0 or m <= curr_pos[1] or curr_pos[1] < 0:
        return False
    return True

def print_board(board):
    for attr in board:
        for v in attr:
            sys.stdout.write(f'{v} ')
        sys.stdout.write('\n')


def bfs(board, start_point, color):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))] 
    q = deque()
    q.append(start_point)
    visited[start_point[0]][start_point[1]] = True
    curr_color = board[start_point[0]][start_point[1]]
    while q:
        curr_pos = q.popleft()
        board[curr_pos[0]][curr_pos[1]] = color
        for direction in directions:
            ny = curr_pos[0] + direction[0]
            nx = curr_pos[1] + direction[1]
           
            if check_boundary(len(board), len(board[0]), (ny, nx)):
                if not visited[ny][nx]:
                    if board[ny][nx] == curr_color:
                        if visited[ny][nx]:
                            continue
                        q.append((ny, nx))

                        visited[ny][nx] = True
    return board

n, m = map(int, sys.stdin.readline().split())
board = init_board(n)
Q = int(sys.stdin.readline())
for _ in range(Q):
    i, j, c = map(int, sys.stdin.readline().split())
    board = bfs(board, (i-1, j-1), c)


print_board(board)

