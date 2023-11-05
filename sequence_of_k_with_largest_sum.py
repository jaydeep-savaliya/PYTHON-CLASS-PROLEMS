import heapq 
class Solution:
    def __init__(self,nums,k): 
        self.nums = nums
        self.k = k
    def maxSubsequence(self,nums:list[int],k:int)->list[int]:
        tuple_heap = []
        for i,val in enumerate(nums):
            if len(tuple_heap)==k:
                heapq.heappushpop(tuple_heap,(val,i))
            else:
                heapq.heappush(tuple_heap,(val,i))
        tuple_heap.sort(key=lambda x:x[1])
        ans = []
        for i in tuple_heap:
            ans.append(i[0])
        return ans
    
nums = [-1,-2,3,4]
k = 3
solution = Solution(nums,k)
ans = solution.maxSubsequence(nums,k)
print(ans)

