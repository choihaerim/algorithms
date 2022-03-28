n = int(input())
answer = 1
for i in range(1, n):
    if i % 2 == 1:
        answer  = (answer * 2) + 1
    else:
        answer = (answer * 2) - 1
print(answer % 10007)