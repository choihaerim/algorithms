import math
 
class Solution:
    def solution(self, price, cost):
        answer = math.inf
        arr = []
        
        for i in range(len(price)):
            sum = 0
            for j in range(len(price)):
                if price[j] >= price[i]:
                    if (price[i] - cost[j]) > 0:
                        sum += (price[i] - cost[j])
                
            
            arr.append(sum)
                
        
            
        if max(arr) == 0:
            return 0
        else:
            id = []
            for i in range(len(arr)):
                if arr[i] == max(arr):
                    id.append(i)
            
            for i in id:
                answer = min(answer, price[i])
            
            return answer