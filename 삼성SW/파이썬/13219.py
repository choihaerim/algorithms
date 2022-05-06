import math

T=int(input())

def check(p,x,y):
    if math.pow((x - 50),2) + math.pow((y - 50),2) > 2500:
        pass
    else:
        degree_y = 90 - (math.atan2(y - 50, x - 50) / math.pi * 180)
        if degree_y < 0:
            degree_y += 360
        if degree_y < p * 360/100:
            return 1
        else:
            return 0
    return 0


for i in range(1,T+1):
    P,X,Y=map(int,input().split())
    print(f"#{i} {check(P,X,Y)}")