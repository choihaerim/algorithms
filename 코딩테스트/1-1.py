#행운의 번호는 2*n 자릿수를 가진 숫자인데, 왼쪽에서부터 n 개의 숫자의 합이 오른쪽에서부터 n 개의 숫자의 합과 같다.
#당신에게 0을 제외한 숫자로만 이루어진 문자열 **s**가 주어진다. 이 문자열의 부분문자열 중 가장 긴 행운의 번호의 길이를 구하시오. 만약 행운의 번호가 없다면 0을 반환하시오.

class Solution:
    def solution(self, number, dictionary):
        dictionary.sort()
        answer = ""
        for n in number:
            for i in range(len(dictionary)):
                if len(dictionary[i]) == int(n):
                    answer += dictionary.pop(i) + " "
                    break
        
        return answer.strip()