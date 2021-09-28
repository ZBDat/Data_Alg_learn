import collections

n = int(input())
edge = [[] for i in range(n)]
a = list(map(int, input().split()))
for i in range(n-1):
    x,y = map(int, input().split())
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)
print(edge)