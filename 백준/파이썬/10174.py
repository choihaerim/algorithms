n = int(input())

for i in range(n):
    text = input().lower()

    if text == text[::-1]:
        print("Yes")

    else:
        print("No")