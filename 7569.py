"""
처음엔 그냥 List:[] 로 작성했으나 시간초과로 Collections 라이브러리 이용했더니 통과
List랑 함수는 같으니 시간 아끼고 싶을 때 효율적임
"""

from collections import deque

# 전역으로 MAP, Queue 설정 굳이 안이래도 됨 하지만, 함수 단위로 나누고 싶어서 이렇게 작성함
Global_map = []
q = deque()


# 6방향 (같은 층에서 4방향 + 위아래층 2방향)
directions = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

# 맵을 초기화 함 입력을 받고, Queue 초깃값 설정 **여기서 Visit Map은 필요없을 것으로 생각되어 초기화 하지 않음
"""
Visit Map이 필요없는 이유-

Map에 1, 0, -1 값만 존재하는데, BFS를 거치면서 각 Map에 도달 시간을 기록해두게 되면 0 값이 있을때에는 Visit하지 않은 것이지만, 어떤 값이 있을때에는 Visit한 것으로 봐도 무방함
BFS는 First-In-First-Out 알고리즘을 따르기에 기록된 값이 가장 빠르게 익을 수 있는 시간임
"""
def init_map(m,n,h):
    for z in range(h):
        y_maps = []
        for y in range(n):
            x_map = list(map(int, input().split()))

            # 처음 queue에 집어 넣을 때, For문 여러번 돌지 않게 미리 Queue에 초깃위치를 지정해줌
            for index, init_position in enumerate(x_map):
                if init_position == 1:
                    q.append((z, y, index))
            
            y_maps.append(x_map)
        Global_map.append(y_maps)


# 맵을 돌아다닐 때, Boundary Check 경계를 나가면 False, 갈 수 있는 위치면 True
def boundary_check(position, m, n, h):
    curr_z, curr_y, curr_x = position
    if curr_z < 0 or curr_z >= h or curr_y < 0 or curr_y >= n or curr_x < 0 or curr_x >= m:
        return False
    return True
    

# BFS로 풀어야 최소 일수를 구할 수 있기에 BFS로 접근함
def sol(m, n, h):
    answer = 0 
    while q:
        curr_z, curr_y, curr_x = q.popleft()
        for direction in directions:
            next_z = curr_z + direction[0]
            next_y = curr_y + direction[1]
            next_x = curr_x + direction[2]

            if boundary_check((next_z, next_y, next_x), m, n, h):
                if Global_map[next_z][next_y][next_x] == 0:
                    Global_map[next_z][next_y][next_x] = Global_map[curr_z][curr_y][curr_x] + 1
                    answer = max(Global_map[next_z][next_y][next_x]-1, answer)
                    q.append((next_z, next_y, next_x))

    for h in Global_map:
        for y in h:
            if 0 in y:
                return -1

    return answer





if __name__=='__main__':
    m,n,h = map(int,input().split())
    init_map(m,n,h)
    print(sol(m,n,h))
    # answering(m,n,h)




    

