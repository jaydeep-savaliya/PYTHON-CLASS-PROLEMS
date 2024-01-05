class Solution:
    def __init__(self,nums):
        self.nums = nums
    def getSumAbsoluteDifferences(self,nums:list[int])->list[int]:
        n = len(nums)
        left = 0
        total = sum(nums)
        ans = []
        for i in range(n):
            right = total - left - nums[i]
            left_count = i
            right_count = n-i-1
            left_total = left_count*nums[i] - left
            right_total = right - right_count*nums[i]
            ans.append(right_total+left_total)
            left+=nums[i]
        return ans
nums = [2,3,5]
solution = Solution(nums)
print(solution.getSumAbsoluteDifferences(nums))