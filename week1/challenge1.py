from collections import deque

directions = [(0,1),(-1,0),(1,0),(0,-1)]
q = deque()

def check_boundary(y, x, n, m):
    if y >= n or y < 0 or x >= m or x < 0:
        return False
    return True

answer = 0 

def dfs(grid, q, d):

    global answer
    
    if len(d) == 0:
        answer = answer + 1
        return

    # print(q, d, answer)
    y, x = q.pop()
    for direction in directions:
        next_y = y + direction[0]
        next_x = x + direction[1]
        
        if check_boundary(next_y, next_x, len(grid), len(grid[0])):
            if grid[next_y][next_x]-grid[y][x] == d[0]:
                q.append((next_y, next_x))
                dfs(grid, q, d[1:])
        
    if len(q) == 0:
        return
    

def solution(grid, d, k):
    answer = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            q.append((y, x))
            dfs(grid, q, d*k)
    return answer

if __name__ == '__main__':
    grid = [[3, 4, 6, 5, 3], [3, 5, 5, 3, 6], [5, 6, 4, 3, 6], [7, 4, 3, 5, 0]]
    d = [1, -2, -1, 0, 2]
    k = 2
    solution(grid, d, k)
    print(answer)
    answer = 0 
    q = deque()
    grid = [[3, 6, 11, 12], [4, 8, 15, 10], [2, 7, 0, 16]]
    d = 	[1, -2, 5]
    k = 3
    solution(grid,d,k)
    print(answer)
    answer = 0
    q = deque()
