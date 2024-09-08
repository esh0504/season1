
MOD = 1000000007

def matmul(a, b):
    new_mat = [[0, 0],[0, 0]]
    new_mat[0][0] = a[0][0] * b[0][0] % MOD + a[0][1] * b[1][0] % MOD
    new_mat[1][0] = a[1][0] * b[0][0] % MOD + a[1][1] * b[1][0] % MOD
    new_mat[0][1] = a[0][0] * b[0][1] % MOD + a[0][1] * b[1][1] % MOD
    new_mat[1][1] = a[1][0] * b[0][1] % MOD + a[1][1] * b[1][1] % MOD
    return new_mat


def sol(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    temp = sol(n // 2)
    if n % 2 == 1:
        return matmul(matmul(temp, temp), sol(1))
    else:
        return matmul(temp, temp)


if __name__ == '__main__':
    n = int(input())
    print(sol(n)[1][0] % MOD)