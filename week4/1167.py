import sys

input = sys.stdin.readline

def init_tree(n):
    tree = [[-1] * n for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(1, len(tmp)-1, 2):
            tree[i][tmp[j]-1] = tmp[j+1]
    return tree



if __name__ == '__main__':
    n = int(input())
    tree = init_tree(n)
