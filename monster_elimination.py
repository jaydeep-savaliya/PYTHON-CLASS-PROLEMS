import heapq
class Solution:
    def __init__(self,dist,speed):
        self.dist = dist
        self.speed = speed
    def eliminateMaximum(self,dist:list[int],speed:list[int])->list[int]:
        heap = []
        ans = 0
        for i in range(len(dist)):
            heap.append(dist[i]/speed[i])
        heapq.heapify(heap)
        while heap:
            if heapq.heappop(heap)<=ans:
                break
            ans+=1
        return ans
dist = [1,3,4]
speed = [1,1,1]
solution = Solution(dist,speed)
print(solution.eliminateMaximum(dist,speed))
