import collections
class Solution:
    def __init__(self,nums,k):
        self.nums = nums
        self.k = k
    def maxSlidingWindow(self,nums:list[int],k:int)->list[int]:
        ans = []
        q=collections.deque()
        for i,num in enumerate(nums):
            while q and q[0]<i-k+1:
                q.popleft()
            while q and nums[q[-1]]<num:
                q.pop()
            q.append(i)
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans
    
solution = Solution([1,3,-1,-3,5,3,6,7],3)
ans=solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(ans)

        