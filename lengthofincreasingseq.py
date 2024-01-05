import bisect
class Solution:
    def __init__(self,nums) -> None:
        self.nums = nums
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [nums[0]]
        for x in nums[1:]:
            if x>lis[-1]:
                lis.append(x)
            else:
                i = bisect.bisect_left(lis,x)
                lis[i] = x
        return len(lis)
nums = [10,9,2,5,3,7,101,18]
sol = Solution(nums)
print(sol.lengthOfLIS(nums))