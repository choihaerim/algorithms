import sys
input=sys.stdin.readline
n,k=map(int,input().split())
d=[0]*(k+1)
for _ in range(n):
    w,v=map(int,input().split())
    #가방 안에 중복해서 넣으면 안되므로 뒤에서부터 넣음
    for i in range(k,w-1,-1):
        d[i]=max(d[i],d[i-w]+v)
print(d[k])