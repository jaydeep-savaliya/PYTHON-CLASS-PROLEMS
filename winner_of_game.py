import collections
class Solution:
    def __init__(self,arr,k):
        self.arr = arr
        self.k = k
    def getWinner(self,arr:list[int],k:int)->list[int]:
        max_element = max(arr)
        queue = collections.deque(arr[1:])
        curr = arr[0]
        winstreak = 0   
        while queue:
            rival = queue.popleft()
            if curr>rival:
                queue.append(rival)
                winstreak+=1
            else:
                queue.append(curr)
                curr = rival
                winstreak = 1
            if curr==max_element or winstreak==k:
                return curr
        return -1

arr = [2,1,3,5,4,6,7]
k = 2
solution = Solution(arr,k)
print(solution.getWinner(arr,k))