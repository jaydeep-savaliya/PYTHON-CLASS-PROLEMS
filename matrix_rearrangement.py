class Solution:
    def __init__(self,matrix):
        self.matrix = matrix
    def largestSubmatrix(self,matrix:list[list[int]])->int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]!=0 and i>0:
                    matrix[i][j]+=matrix[i-1][j]
            new_matrix = sorted(matrix[i],reverse=True)
            for x in range(m):
                ans = max(ans,new_matrix[x]*(x+1))
        return ans
matrix = [[0,0,1],[1,1,1],[1,0,1]]
solution = Solution(matrix)
print(solution.largestSubmatrix(matrix))