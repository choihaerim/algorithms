T = 10 
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        min_value = 987654321
        for j in range(5):
            if j != 2:
                if arr[i] - arr[i-2+j] < min_value:
                    min_value = arr[i] - arr[i-2+j]
        if min_value > 0 :
            ans += min_value
    print("#{} {}".format(tc, ans))