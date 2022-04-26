def solution(N):
   tiles = [1 for _ in range(N)]
   before = tiles[1]
   before_back = tiles[0]
   for i in range(N):
       if i == 0 or i == 1:
           continue
       tiles[i] = before+ before_back
       before = tiles[i]
       before_back = tiles[i-1]
   
   case = [4]
   for i in range(N):
       if i==0:
           continue
       before = case[i-1]
       now = before + tiles[i] *2  
       case.append(now)
   
   answer = case[N-1] # case 배열의 마지막이 N개의 타일들로 구성된 직사각형의 둘레
   return answer