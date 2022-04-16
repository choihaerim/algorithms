import collections


T = 10
for t in range(1, T+1):
    tc = int(input())
    queue2 = collections.deque(list(map(int, input().split())), maxlen=8)

    i = 1
    while True:
        if i > 5:
            i = 1
        t = queue2.popleft() - i
        if t <= 0:
            queue2.append(0)
            break
        queue2.append(t)
        i += 1

    print("#{}".format(tc), end=" ")
    for q in queue2:
        print("{}".format(q), end=" ")
    print()