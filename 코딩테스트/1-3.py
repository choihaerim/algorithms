"""
당신은 학교에서 집까지 도시를 거쳐 걸어가고 있다.
도시는 무한히 크며 모든 int X값에는 수직 도로가 놓여있고 모든 int Y에는 수평 도로가 놓여있다.
당신은 현재 (0, 0)에 있으며 (X, Y)에 있는 집에 가려고 한다. 집까지 가는 방법에는 두가지가 있다: 수평 혹은 수직으로 인접한 교차로를 거쳐 (int walkTime 초가 걸린다) 도로를 따라 걷는 것과 몰래 대각선으로 건너 (int sneakTime 초가 걸린다) 반대쪽 모서리로 가는 방법이 있다.
이미지에 나와있는 것처럼 걷거나 대각선을 가로지르는 8가지 방향 어느쪽으로도 가는 것이 가능하다
"""

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