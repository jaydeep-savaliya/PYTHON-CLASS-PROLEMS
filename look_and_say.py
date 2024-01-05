class Solution:
    def __init__(self,n):
        self.n = n
    def generateSequence(self,n:int)->str:
        dp = ['']*(n+1)
        dp[1] = '1'
        for i in range(2,n+1):
            prev = dp[i-1]
            curr = ''
            j = 0
            while j<len(prev):
                count = 1
                while j+1<len(prev) and prev[j] == prev[j+1]:
                    count+=1
                    j+=1
                curr+=str(count) + prev[j]
                j+=1
            dp[i] = curr
        return dp[n]
n = 4
sol = Solution(n)
print(sol.generateSequence(n))
