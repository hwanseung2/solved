# N에 있는 원소를 x라고 두고 M에 있는 원소를 y로 뒀을 때, N<=x,y<=M이고
# 서로 겹칠 수 없다. 순열을 사용하자.

import math

def comb(left_site, right_site):
    Mf = math.factorial(right_site)
    Nf = math.factorial(left_site)
    mom = math.factorial(right_site - left_site)
    return (Mf // (Nf*mom))


T = int(input())
for t in range(T):
    N,M = map(int, input().split(" "))
    print(comb(N,M))
