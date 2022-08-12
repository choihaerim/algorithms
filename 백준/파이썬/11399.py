num_ppl = int(input())
waiting_time = list(map(int, input().split()))
answer = 0
waiting_time.sort()

for i in range(num_ppl):
    answer += waiting_time[i] * (num_ppl-i)

print(answer)