class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countOfAlphaInS, countOfAlphaInT = {}, {} 

        for i in range(len(t)):
            countOfAlphaInS[s[i]] = 1 + countOfAlphaInS.get(s[i],0)
            countOfAlphaInT[t[i]] = 1 + countOfAlphaInT.get(t[i],0)
        return countOfAlphaInS == countOfAlphaInT
        # setOfs = set(s);
        # setOft = set(t);
        # return (set(s) == set(t) and len(s)==len(t));
        