class Solution:
    def __init__(self,s):
        self.s = s
    def timeConversion(self,s:str)->str:
        if s[-2:0]=='PM':
            if int(s[:2])==12:
                return f"{s[:-2]}"
            return f"{int(s[:2]) + 12}{s[2:-2]}"
        elif int(s[:2])==12:
            return f"00{s[2:-2]}"
        else:
            return f"{s[:-2]}"
s = "07:05:45PM"
solutin = Solution(s)
print(solutin.timeConversion(s))