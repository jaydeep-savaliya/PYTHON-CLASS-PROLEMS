import collections

class Solution:
    def __init__(self,nums) -> None:
        self.nums = nums
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        ans = []
        fre = collections.defaultdict(int)
        for i in nums:
            if fre[i]>=len(ans):
                ans.append([])
            ans[fre[i]].append(i)
            fre[i]+=1
        return ans
nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4]
sol = Solution(nums)
print(sol.findMatrix(nums))