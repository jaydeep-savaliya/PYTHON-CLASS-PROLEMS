class Solution:
    def __init__(self,n):
        self.n = n
    def remove_trail(self,n:int)->int:
        
        n = n+1
        while n%10==0:
            n = n//10
        return n
        
n = 19
solution = Solution(n)
print(solution.remove_trail(n))