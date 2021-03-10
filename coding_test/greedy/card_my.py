n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
min_list = []
for list_ in arr:
    min_list.append(min(list_))
print(max(min_list))