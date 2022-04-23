import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  tree[a].append(b)
  inDegree[b] += 1

q = []
for i in range(1,n+1):
  if inDegree[i] == 0: # 차수가 0 인 문제를 최소 힙에 push
    heapq.heappush(q, i)

result = []
while q:
  a = heapq.heappop(q)
  result.append(a)
  for i in tree[a]: # 문제쌍 B가 있는 경우에
    inDegree[i] -= 1 # 문제쌍 B의 차수를 1 줄이고
    if inDegree[i] == 0: # 문제쌍 B의 차수가 0 이면
      heapq.heappush(q, i) # 최소힙에 push

print(*result) # *result(*args) : 가변 위치인자 (임의 개수의 위치 인자를 tuple 형태의 변수로 저장)