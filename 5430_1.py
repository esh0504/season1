def printArr(arr):
    print('[', end='')
    for i in range (len(arr)):
        if i==0:
            print(arr[i],end='')
            continue
        print(f',{arr[i]}',end='')
    print(']')

def sol(p, arr):
    try:
        arr = list(map(int, arr))
    except:
        arr = []

    if p.count('D') > len(arr):
        print('error')
        return

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

            if flag:
                left_cnt += 1
            else:
                right_cnt -= 1

    if not flag:
        if left_cnt == 0:
            printArr(arr[::-1][-right_cnt:])
            return
        printArr(arr[::-1][-right_cnt:-left_cnt])
    else:
        if right_cnt==0:
            printArr(arr[left_cnt:])
            return
        printArr(arr[left_cnt:right_cnt])

if __name__ == '__main__':
    testCase = int(input())
    for i in range(testCase):
        p = list(input())
        n = int(input())
        arr = list(input()[1:-1].split(','))
        sol(p, arr)
