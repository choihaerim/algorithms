class Solution:
    def solution(self, x, y, w, s):
        move1 = (x + y) * w
 
        if (x + y) % 2 == 0:
            move2 = max(x, y) * s
        else:
            move2 = (max(x, y) - 1) * s + w
            
        move3 = (min(x, y) * s) + ((max(x, y) - min(x, y)) * w)
        
        res = min(min(move1, move2), move3)
        
        return res