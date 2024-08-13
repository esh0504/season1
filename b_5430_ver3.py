def sol(p, arr):
    if len(arr)==1 and arr[0]=='' and 'D' in p:
        print('error')
        return
    if len(arr)==1 and arr[0]=='' and 'D' not in p:
        arr = []
    else:
        arr = list(map(int, arr))
    flag = True
    left_cnt = 0
    right_cnt = 0
    for attr in p:
        if attr == 'R':
            if flag:
                flag = False
            else:
                flag = True
        else:
            if left_cnt + right_cnt == len(arr) and 'D' in p[left_cnt+right_cnt:]:
                print('error')
                return
            if flag:
                left_cnt += 1
            else:
                right_cnt -= 1

    if not flag:
        if left_cnt == 0:
            print(arr[::-1][-right_cnt:])
            return
        print(arr[::-1][-right_cnt:-left_cnt])
    else:
        if right_cnt==0:
            print(arr[left_cnt:])
            return
        print(arr[left_cnt:right_cnt])

if __name__ == '__main__':
    testCase = int(input())
    for i in range(testCase):
        p = list(input())
        n = int(input())
        arr = list(input()[1:-1].split(','))
        sol(p, arr)
