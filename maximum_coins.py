import collections

from pyparsing import col
class Solution:
    def __init__(self,piles):
        self.piles = piles
    def maxCoins(self,piles:list[int])->list[int]:
        piles.sort()
        # queue = collections.deque(piles)
        ans = 0
        # while queue:
        #     queue.pop()
        #     ans+=queue.pop()
        #     queue.popleft()
        for i in range(len(piles)//3,len(piles),2):
            ans+=piles[i]
        return ans
piles =  [9,8,7,6,5,1,2,3,4]
solution = Solution(piles)
print(solution.maxCoins(piles))