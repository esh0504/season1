def sol(p, arr):
    if len(arr) == 0 or arr[0]=='':
        if len(p) > 0:
            print('error')
            return
    if len(p) == 0:
        print(arr)
        return

    for cmd in p:
        if cmd == 'D':
            return sol(p[1:], arr[1:])
        else:
            return sol(p[1:], arr[::-1])

if __name__ == '__main__':
    testCase = int(input())
    for i in range(testCase):
        p = list(input())
        n = int(input())
        arr = list(input()[1:-1].split(','))
        sol(p, arr)
