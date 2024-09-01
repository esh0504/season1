from collections import deque

def init_board(v):
    return [[-1 for _ in range(v)] for _ in range(v)]

if __name__ == '__main__':
    v = int(input())
    board = init_board(v)
    
    for _ in range(v):
        info = list(map(int, input().split()))
        src = info[0]
        
        for index in range(1, len(info)-1, 2):
            
            board[src-1][info[index]-1] = info[index + 1]
            board[info[index]-1][src-1] = info[index + 1]

    