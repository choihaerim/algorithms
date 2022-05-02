T = int(input())

for t in range(1, T + 1):
    N,M=map(int,input().split())

    graph=[list(map(int,input().split())) for _ in range(N)]

    res=[]

    for i in range(N):
        for j in range(N): 
            Sum=0
            if i+M<=N and j+M<=N:
                for k in range(i, i + M):
                    for l in range(j, j + M):
                        Sum += graph[k][l]
                res.append(Sum)

    print(f"#{t} {max(res)}")