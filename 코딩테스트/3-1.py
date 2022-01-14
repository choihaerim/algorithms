"""두개의 정수 a와 b에 대하여 a와 b 사이에 있는 모든 정수가 한번씩만 등장했을 때, 이를 정수가 연속한다고 말한다.
당신의 아들이 연속된 양의 정수를 임의의 순서대로 종이에 쓰고 있었다. 이 때, 각 숫자는 정확히 한번만 쓰여졌다. 그리고나서 그 중 하나의 숫자를 지웠다. 아들은 어느 숫자를 지웠는지 맞춰보라고 한다.
예를 들어, (10, 7, 12, 8, 11)이 종이에 남아 있었다면 지운 숫자는 9가 된다. 만약 남은 숫자가 (2, 3)이라면 지운 숫자는 1 혹은 4가 된다. 남은 숫자가 (3, 6)이라면 당신의 아들이 실수한 것이다.
종이에 남은 숫자는 vector<int> numbers로 주어진다. 당신의 아들이 지웠을 가능성이 있는 모든 숫자를 정수 배열의 형태로 반환하여라. 숫자들은 높은 차순으로 정렬되어야하며 중복되는 숫자는 없어야 한다. 만약 아들이 실수를 했다면 아무것도 들어있지 않은 정수 배열을 반환하여라."""

class Solution:
    def solution(self, numbers):
        beanswer = []
        answer = []
        numbers.sort()
        
        #중간에서 뽑았을 때
        for i in range(1,len(numbers)):
            if numbers[i] > numbers[i-1]+1:         # 두 수의 차이가 1보다 클 경우
                if numbers[i] == numbers[i-1]+2:    # 차이가 2인 경우
                    beanswer.append([numbers[i-1],numbers[i]]) # 가능성있는 두 수 배열에 넣기
                else:
                    return answer                    # 2보다 크게 나는 경우 빈 배열 반환
            elif numbers[i] == numbers[i-1]:
                return answer
        
        if len(beanswer) == 1:                       # 가능성있는 두 수가 한쌍만 있어야 함
            answer.append(beanswer[0][0]+1)
            return answer
        elif len(beanswer) > 1:
            return answer
        
        # 중간이 잘 정렬되어 있을 때
        if numbers[0] == 1:
            answer.append(numbers[len(numbers)-1]+1)
            return answer
        else:
            answer.append(numbers[0]-1)
            answer.append(numbers[len(numbers)-1]+1)
            return answer