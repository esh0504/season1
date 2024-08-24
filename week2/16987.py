
def count(S):
    answer = 0
    for attr in S:
        if attr <= 0:
            answer += 1
    return answer

answer = 0
def dfs(S, W, grib):
    global answer
    # print(S, W, grib, answer)
    if count(S) == len(S):
        return len(S)
    if grib == len(S):
        return count(S)
    if grib == len(S)-1 and count(S) == len(S)-1:
        return len(S)-1
        
    for i in range(len(S)):
        if S[grib] <= 0:
            answer = max(dfs(S, W, grib + 1), answer)
            continue
        if i == grib:
            continue
        if S[i] <= 0:
            continue
        S[i] = S[i] - W[grib]
        S[grib] = S[grib] - W[i]
        answer = max(dfs(S, W, grib + 1), answer)
        S[i] += W[grib]
        S[grib] += W[i]

    return count(S)





if __name__=='__main__':
    N = int(input())
    S = []
    W = []
    for i in range(N):
        s, w = map(int, input().split())
        S.append(s)
        W.append(w)
    dfs(S,W,0)
    print(answer)
    