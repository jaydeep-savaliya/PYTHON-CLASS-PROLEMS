class Solution:
    def __init__(self,pref):
        self.pref = pref
    def findArary(self,pref:list[int])->list[int]:
        prev = pref[0]
        for i in range(1,len(pref)):
            pref[i]^=prev
            prev^=pref[i]
        return pref
pref=[5,2,0,3,1]
solution = Solution(pref)
ans = solution.findArary(pref)
print(ans)