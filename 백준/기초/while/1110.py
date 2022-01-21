input_data = int(input())
count = 0
N = input_data
num = N

while True:
    num_1 = num // 10
    num_2 = num % 10
    num_3 = (num_1 + num_2) % 10
    num = (num_2 * 10) + num_3
    count += 1

    if num == N:
        print(count)
        break