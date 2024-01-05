from math import ceil
from typing import Counter


class Solution:
    def __init__(self,nums) -> None:
        self.nums = nums
    def minOperations(self,nums:list[int])->int:
        ans = 0
        counter = Counter(nums)
        for c in counter:
            if c==1:
                return -1
            ans+=ceil(c/3)
        return ans
    

nums = [2,3,3,2,2,4,2,3,4]
sol = Solution(nums)
print(sol.minOperations(nums))