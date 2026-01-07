class Solution:
    def secondHighest(self, s: str) -> int:
        s=set(s)
        a=[]
        for char in s:
            if char.isnumeric() :
                a.append(int(char))
        a.sort()
        if len(a)<2:
            return -1
        return a[len(a)-2]