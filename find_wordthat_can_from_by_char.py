import collections
class Solution:
    def __init__(self,words:list[str],chars:str):
        self.words = words
        self.chars = chars
    def countCharacters(self,words:list[str],chars:str)->int:
        count = collections.defaultdict(int)
        for i in chars:
            count[i]+=1
        ans = 0
        for i in words:
            word_count = collections.defaultdict(int)
            for j in i:
                word_count[j]+=1
            good = True
            for c,fre in word_count.items():
                if count[c]<fre:
                    good = False
                    break
            if good:
                ans+=len(i)
        return ans
words = ["cat","bt","hat","tree"]
chars = "atach"
solution = Solution(words,chars)
print(solution.countCharacters(words,chars))