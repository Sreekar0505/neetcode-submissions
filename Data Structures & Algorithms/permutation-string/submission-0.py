class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = len(s1)
        n = len(s2)
        l = 0

        def checkPerm(ind):
            return sorted(s1) == sorted(s2[l:l+d])
        while l+d-1 < n:
            if checkPerm(l):
                return True
            l+=1
        return False