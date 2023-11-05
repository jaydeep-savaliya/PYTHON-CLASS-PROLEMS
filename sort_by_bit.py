
class Solution:
    def __init__(self,nums):
        self.nums = nums
    def sortByBit(self,nums:list[int])->list[int]:
        def sort_by_bit(nums):
            count_bit = bin(nums).count('1')
            return(count_bit,nums)
        nums.sort(key=sort_by_bit)
        return nums
nums=[0,1,2,3,4,5,6,7,8]
solution = Solution(nums)
ans = solution.sortByBit(nums)
print(ans)