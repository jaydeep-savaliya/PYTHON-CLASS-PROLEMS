class Solution:
    def __init__(self,arr,k):
        self.arr = arr
        self.k = k
    def maximumSum(self,arr:list[int],k:int)->int:
        n = len(arr)
        pref = [0]*(n+1)
        ans = 0
        arr.sort()
        for i in range(len(arr)):
            pref[i+1] = pref[i]+arr[i]
        for i in range(k+1):
            ans = max(ans,(pref[n-i]-pref[2*(k-i)]))
        return ans
arr=[2,5,1,10,6]
k = 1
solution = Solution(arr,k)
print(solution.maximumSum(arr,k))