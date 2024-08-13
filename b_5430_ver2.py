def sol(p, arr):
    if len(arr)==1 and arr[0]=='' and len(p)>0:
        print('error')
        return

    if len(p) > 2:
        if p[0]=='R' and p[1]=='R':
            sol(p[2:], arr)
        elif p[0]=='R' and p[1]=='D':
            arr = arr[:-1]
            sol(p[2:], arr[::-1])
        elif p[0]=='D' and p[1]=='D':
            sol(p[2:], arr[2:])
        else:
            sol(p[2:],arr[1:][::-1])
    else:
        if len(p)==0:
            print(arr)
            return
        elif p[0]=='R':
            sol(p[1:], arr[::-1])
            return
        else:
            if len(arr)==0 and len(p) > 0:
                print('error')
                return
            sol(p[1:],arr[1:])



if __name__ == '__main__':
    testCase = int(input())
    for i in range(testCase):
        p = list(input())
        n = int(input())
        arr = list(input()[1:-1].split(','))
        sol(p, arr)
