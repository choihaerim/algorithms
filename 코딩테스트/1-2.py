class Solution:
    def solution(self, s):
        
        for i in range(len(s)):
            if s[i:]==s[i:][::-1]:
                break
        
        return len(s)+i