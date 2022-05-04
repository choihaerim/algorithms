# 1에서 9까지의 모든 곱을 리스트에 저장하고 주어진 숫자가 리스트에 존재하는지 확인하는 방식으로 해결하기
List=[]

for i in range(1,10):
    for j in range(1,10):
        List.append(i*j)

my_List=list(set(List)) #순서는 상관x

T=int(input())

for i in range(1,T+1):
    Num=int(input())
    if Num in my_List:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")


# 주어진 숫자를 9이하의 수로 나누었을 때 나눈 값이 9이하이며 정수인지 판별하기
T=int(input())

for i in range(1,T+1):
    Num=int(input())
    check=False
    for j in range(1,10):
        if Num/j<=9 and (Num/j).is_integer():
            check=True

    if check:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")