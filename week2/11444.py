def matmul(matrix1, matrix2):
    new_mat = []
    for row in range(len(matrix1)):
        tmp_mat = []
        for row2 in range(len(matrix1)): 
            c = 0
            for col in range(len(matrix1[0])):
                c += matrix1[row][col] * matrix2[col][row2]
            c %= 1000000007
            tmp_mat.append(c)
        new_mat.append(tmp_mat)
    return new_mat

def sol(n):
    matrix = [[1, 1],[1, 0]]
    if n%2==1:

    

if __name__ == '__main__':
    n = int(input())
    sol(4)