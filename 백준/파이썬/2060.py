n = int(input())
m = int(input())

computer = dict()
virus = []
check_virus = []

def check(y):
    if y in computer:
        for i in computer[y]:
            if i not in virus and i not in check_virus:
                virus.append(i)
    return 0
for i in range(m):
    x, y = map(int, input().split())
    if x not in computer:
        computer[x] = list()
    if y not in computer:
        computer[y] = list()
    computer[x].append(y)
    computer[y].append(x)

for i in computer[1]:
    virus.append(i)
    while virus:
        a = virus.pop(0)
        if a not in check_virus:
            check_virus.append(a)
        check(a)

print(len(check_virus) - 1) 