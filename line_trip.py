from networkx import difference


class Solution:
    def __init__(self,arr,x):
        self.arr = arr
        self.x = x
    def findMinimumFualcapacity(self,arr:list[int],x:int)->int:
        diff = 2*(x-arr[len(arr)-1])
        ans = diff
        if len(arr)==1 and arr[0]>diff:
            return arr[0]
        for i in range(1,len(arr)):
            difference = arr[i]-arr[i-1]
            ans = max(ans,difference)
        return ans


arr=[1,2,5]
x = 6
solution = Solution(arr,x)
print(solution.findMinimumFualcapacity(arr,x))