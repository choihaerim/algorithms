"""
로봇이 평면 위에서 다음과 같은 명령을 받아서 움직이고 있다.
LEFT – 왼쪽으로 90도 회전
RIGHT – 오른쪽으로 90도 회전
TURN AROUND – 반 바퀴 회전 (180도 회전)
LEFT X – 왼쪽으로 X도 회전 (X는 양의 정수)
RIGHT X – 오른쪽으로 X도 회전 (X는 양의 정수)
HALT – 명령어를 수행 중지, 앞으로 모든 명령을 수행하지 않는다
로봇의 명령어는 문자열의 배열 **instructions**로 주어진다. 명령을 전부 수행 한 다음에 로봇의 방위각을 구하시오.
(방위각은 북쪽을 기존으로 로봇이 바라보는 각도이며, 방위각은 시계방향으로 측정이 된다. 즉, 로봇이 서쪽을 바라보고 있다면 방위각은 270이 된다.)
"""
class Solution:
    def solution(self, instructions):
        answer = 0
        for c in instructions:
            if c == "LEFT":
                answer -= 90
            elif c == "RIGHT":
                answer += 90
            elif c == "TURN AROUND":
                answer += 180
            elif c == "HALT":
                break
            else:
                d, n = c.split(" ")
                if d == "LEFT":
                    answer -= int(n)
                elif d == "RIGHT":
                    answer += int(n)
        return answer % 360