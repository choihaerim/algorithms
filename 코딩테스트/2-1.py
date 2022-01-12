"""
당신에게 적군의 코드를 해석하라는 비밀 미션이 주어졌다. 당신은 그들이 메세지를 다음과 같은 방법으로 암호화한다는 것을 이미 알아냈다.
'a'와 'z'사이의 알파벳을 두자리수 01과 26 사이의 숫자에 할당한다.
메세지는 각 알파벳을 할당된 숫자로 변환하여 암호화된다.
예를 들어, 't'는 20에 할당되고, 'e'는 05에 할당되고, 's'는 19에 할당되어 "test"는 "20051920"으로 암호화된다. 모든 원본 메세지는 소문자만으로 구성되어 있다.

주어진 **code** 에는 숫자와 문자의 할당이 나타나 있다.
첫번째 문자는 01에 할당되고, 두번째 문자는 02에 할당되는 식으로 26까지 이어진다.
또한 주어진 **message** 에는 암호화되지 않은 원본 메세지 혹은 암호화된 메시지가 있다.
만약 원본 메세지가 주어졌다면 메세지를 암호화하여 반환하고, 암호화된 메세지가 주어졌다면 원본 메세지를 반환하라.
"""

class Solution:
    def solution(self, code, message):
        rule = dict()
        
        for idx, c in enumerate(code):
            rule[c] = str(idx + 1).zfill(2)
            rule[str(idx + 1).zfill(2)] = c
            
            answer = ""
            
        if message[0].isdigit():
            for idx in range(len(message) // 2):
                answer += rule[message[2*idx : 2*idx + 2]]
        
        else:
            for m in message:
                answer += rule[m]
                
        return answer