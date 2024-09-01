import sys
from collections import deque

def init_board(n, m):
    board = []
    ghost = []
    curr_pos = (0, 0)
    for i in range(n):
        tmp = sys.stdin.readline()
        board.append(tmp)
        for j in range(m):
            if tmp[j] == 'G':
                ghost.append((i, j))
            elif tmp[j] == 'N':
                curr_pos = (i, j)
    return board, curr_pos,  ghost

def boundary_check(n, m, curr_pos):
    if n <= curr_pos[0] or 0 > curr_pos[0] or m <= curr_pos[1] or 0 > curr_pos[1]:
        return False
    return True
    
def ghost_check(ghosts, curr_pos, cnt):
    for ghost in ghosts:
        if abs(curr_pos[0] - ghost[0]) + abs(curr_pos[1] - ghost[1]) <= cnt:
            return False
    return True

def bfs(board, pos, ghost, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    visited[pos[0]][pos[1]] = True
    q = deque()
    q.append((pos, 0))
    while q:
        curr_pos, cnt = q.popleft()
        for direction in directions:
            ny = curr_pos[0] + direction[0]
            nx = curr_pos[1] + direction[1]
            if boundary_check(n, m, (ny, nx)):
                if board[ny][nx] == '.' and visited[ny][nx]==False:
                    q.append(((ny, nx), cnt + 1))
                    visited[ny][nx] = True
                elif board[ny][nx] == 'D' and ghost_check(ghost, (ny, nx), cnt + 1):
                    return 'Yes'
    return 'No'
                    
                    

n, m = map(int, sys.stdin.readline().split())
board, curr_pos, ghost = init_board(n, m)

sys.stdout.write(f'{bfs(board, curr_pos, ghost, n, m)}')