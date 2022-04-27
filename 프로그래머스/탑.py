def solution(heights):
   hi_list = [(h, i) for (i, h) in enumerate(heights)]
   hi_list.reverse()
   answer = [0] * len(heights)
​
   while hi_list:
       top = hi_list.pop(0)
       if hi_list:
           for i in range(len(hi_list)):
                   if top[0] < hi_list[i][0]:
                       if answer[top[1]] == 0:
                           answer[top[1]]= hi_list[i][1] + 1
​
   return answer