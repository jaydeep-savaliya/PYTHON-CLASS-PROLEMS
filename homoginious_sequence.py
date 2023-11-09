class Solution:
    def __init__(self,s):
        self.s = s
    def countHomogenous(self,s:list[str])->int:
        ans = 0
        streak = 0
        mod = 10**9 + 7
        for i in range(len(s)):
            if i==0 or s[i]==s[i-1]:
                streak+=1
            else:
                streak=1
            ans = (ans+streak)%mod
        return ans
solution=Solution(s="abbcccaa")
print(solution.countHomogenous(s="abbcccaa"))