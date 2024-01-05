class Solution:
    def __init__(self,n):
        self.n = n 
    def hammingWeight(self,n: int)->int:
        ans = 0
        return n.bit_count()
n = 1001
solution = Solution(int(n))
print(solution.hammingWeight(int(n)))