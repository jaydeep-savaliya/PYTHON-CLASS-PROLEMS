class Solution:
    def __init__(self,points:list[list[int]]):
        self.points = points
    def minTimeToVisitAllPoints(self,points:list[list[int]])->int:
        ans = 0
        for i in range(len(points)-1):
            a,b = points[i]
            x,y = points[i+1]
            ans+=max(abs(x-a),abs(y-b))
        return ans
points = [[1,1],[3,4],[-1,0]]
solution = Solution(points)
print(solution.minTimeToVisitAllPoints(points))