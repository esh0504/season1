from collections import deque

directions = [(1,0),(-1,0),(0,1),(0,-1)]
def init_grid(n, m):
    grid = []
    for y in range(n):
        grid.append(list(input()))
    return grid

def boundary_check(y, x, n, m):
    if y>=n or y < 0 or x >= m or x < 0:
        return True
    return False

def bfs(grid):
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0] * 2 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    visited[0][0][0] = 1

    while q:   
        y, x, z = q.popleft()
        if y == len(grid) - 1 and x == len(grid[0]) - 1:
            return visited[y][x][z]
        
        for direction in directions:
            Y = y + direction[0]
            X = x + direction[1]
            if boundary_check(Y, X, len(grid), len(grid[0])):
                continue

            if grid[Y][X] == '0' and visited[Y][X][z] == 0:
                visited[Y][X][z] = visited[y][x][z] + 1
                q.append((Y, X, z))
            elif grid[Y][X] == '1' and z == 0:
                visited[Y][X][1] = visited[y][x][0] + 1
                q.append((Y, X, 1))

            

    return -1
                    

            

if __name__=='__main__':
    n, m = map(int, input().split())
    grid = init_grid(n,m)
    answer = bfs(grid)
    print(answer)
    