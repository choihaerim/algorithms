num = int(input())
result = 1
temp = 1

while temp <= num:
    result = temp * result
    temp += 1

print(result)