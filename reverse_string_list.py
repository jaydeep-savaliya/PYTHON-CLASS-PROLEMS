class Solution:
    def __init__(self,s):
        self.s = s
    def reverse_str(self,s:list[str])->list[str]:
        i = 0
        j = len(s)-1
        while(i<=j):
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        return s
s = ["h","e","l","l","o"]
solution = Solution(s)
print(solution.reverse_str(s))