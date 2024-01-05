class Solution:
    def __init__(self,arr) -> None:
        self.arr = arr
    def diagonalDifference(self,arr:list[list[int]])->int:
        first = 0
        last = 0
        for i in range(len(arr)):
            first = first + arr[i][i]
            last = last + arr[len(arr)-i-1][i]
        return abs(first-last)
arr = [[11,2,14],[4,5,6],[10,8,-2]]
solution = Solution(arr)
print(solution.diagonalDifference(arr))