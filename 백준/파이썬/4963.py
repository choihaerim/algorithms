from collections import deque

def check(a, b):
    map1[a][b]
    queue = deque()
    queue.append([a, b])
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            x = a + move[i][0]
            y = b + move[i][1]
            if 0 <= x < h and 0 <= y < w and map1[x][y] == 1:
                map1[x][y] = 0
                queue.append([x,y])
    
move = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, -1], [1, 1], [-1, 1]]

while True:
    w, h = map(int, input().split())
    
    map1 = []
    answer = 0
    
    if w == 0 and h == 0:
        break
    for i in range(h):
        map1.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if map1[i][j] == 1:
                check(i, j)
                answer += 1            
    print(answer)