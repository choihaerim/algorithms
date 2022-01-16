"""스미드 교수는 논리 수업을 가르친다. 어느 날 그는 다음과 같은 문장을 칠판에 썼다.
이 문장들 중 정확히 a개의 문장이 참이다.
이 문장들 중 정확히 b개의 문장이 참이다.
이 문장들 중 정확히 c개의 문장이 참이다.
a, b, c 등은 각각 숫자이다. 그리고 그는 학생들에게 이 중 몇개의 문장이 참인지 물어보았다.
주어진 정수 배열 vector<int> statements에 Smith 교수가 쓴 숫자들이 적혀있다. 모두 몇 개의 문장이 참인지 리턴하시오.
만약 가능한 답이 두개 이상이라면 그 중 더 큰 숫자를 반환하여라. 가능한 답이 없다면 –1을 리턴하시오."""

class Solution:
    def solution(self, statements):
        for i in reversed(list(set(statements))):
            if statements.count(i)==i:
                return i
        return -1 if i==0 else 0

