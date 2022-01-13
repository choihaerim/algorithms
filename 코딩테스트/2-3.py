"""
생각 경시 대회를 축하하기 위해서 전통적으로 초에 불을 붙인다. 대회 첫째날밤에는 하나의 초에 불을 붙인다. 저녁이 끝나면 불을 끈다. 다음날마다 전날보다 불을 붙이는 초의 개수를 하나씩 늘려서 (1을 기준으로) n번째날 밤에는 n개의 초에 불을 붙인다 (아침에는 모든 초의 불을 끈다).
매일밤 불을 붙일때마다 초의 높이는 1씩 줄어든다. 높이가 0이 되면 더 이상 사용할 수 없다.

주어진 **candles** 의 i번째 요소는 i번째 양초의 높이는 나타낸다.
새로운 양초를 구입하지 않고 최대 며칠밤을 축하할 수 있는지 구하여라.
예를 들어, 높이 2의 초 3개를 가지고 있다면, 첫째날 초 하나를 밝히고, 나머지 두개를 둘째날 밝히고, 셋째날에 모든 초를 밝혀 3일동안 축하할 수 있다.
"""

class Solution:
    def solution(self, candles):
        days = 1
        while True:
            candles.sort(reverse = True)
        
            for idx in range(days):
                candles[idx] -= 1
                if candles[idx] < 0:
                    return days - 1
            if days == len(candles):
                return days
            
            days += 1