from pickletools import long1


class Solution:
    def __init__(self,arr):
        self.arr = arr
    def bigsum(self,arr:list[int])->long1:
        ans = 0
        for i in range(len(arr)):
            ans+=arr[i]
        return ans
arr = [1000000001, 1000000002 ,1000000003 ,1000000004, 1000000005]
solution = Solution(arr)
print(solution.bigsum(arr))