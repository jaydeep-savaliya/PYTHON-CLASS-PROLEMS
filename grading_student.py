
class Solution:
    def __init__(self,grade):
        self.grade = grade
    def findGrades(self,grade:list[int])->list[int]:
        ans = []
        for i in grade:
            if i<38:
                ans.append(i)
            else:
                if i%5==3:
                    ans.append(i+2)
                elif i%5==4:
                    ans.append(i+1)
                else:
                    ans.append(i)
        return ans
grade = [73,68,45]
solution = Solution(grade)
print(solution.findGrades(grade))