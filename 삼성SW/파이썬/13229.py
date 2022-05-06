T=int(input())

List=["MON","TUE","WED","THU","FRI","SAT","SUN"]

for i in range(1,T+1):
    Input=input()
    if Input=="SUN":
        print(f"#{i} 7")
        continue
    res=6-List.index(Input)
    print(f"#{i} {res}")