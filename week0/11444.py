

if __name__ == '__main__':
    n = int(input())
    pre_answer = 1
    answer = 1
    for i in range(3,n+1):
        tmp_answer = answer
        answer = pre_answer + answer
        pre_answer = tmp_answer%1000000007
    print(answer%100000007)
        