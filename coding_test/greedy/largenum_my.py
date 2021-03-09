N, M, K = input().split(" ")
N, M, K = int(N), int(M), int(K)
arr = list(map(int, input().split()))

arr.sort()
sum = 0
cnt = 0
flag = 1
for m in range(M):
    if flag == 1:
        sum += arr[-1]
        cnt +=1
        if cnt == K:
            flag = 0
            cnt = 0
    else:
        sum += arr[-2]
        flag = 1
print(sum)
    