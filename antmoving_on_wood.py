class Solution:
    def __init__(self,n,left,right):
        self.n = n
        self.left = left
        self.right = right
    def getLastMoment(self,n:int,left:list[int],right:list[int])->list[int]:
        ans = 0
        for i in left:
            ans = max(ans,i)
        for j in right:
            ans = max(ans,n-j)
        return ans
n = 7
left = []
right = [0,1,2,3,4,5,6,7]
solution = Solution(n,left,right)
print(solution.getLastMoment(n,left,right))