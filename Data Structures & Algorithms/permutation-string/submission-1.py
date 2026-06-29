class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = len(s1)
        n = len(s2)
        l = 0

        count_s1 = {}
        for i in s1:
            count_s1[i] = count_s1.get(i,0) + 1

        def checkPerm(ind):
            count_s2 = {}

            for i in s2[ind:ind+d]:
                count_s2[i] = count_s2.get(i,0) + 1
            
            return count_s1 == count_s2

        while l+d-1 < n:
            if checkPerm(l):
                return True
            l+=1
        return False