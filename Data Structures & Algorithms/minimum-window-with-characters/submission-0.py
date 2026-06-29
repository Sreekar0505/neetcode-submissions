class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0

        n = len(s)

        count_t = {}

        for i in t:
            count_t[i] = count_t.get(i,0) + 1

        def check(l,r):
            count_s = {}
            for i in s[l:r]:
                count_s[i] = count_s.get(i,0) + 1
            for key in count_t.keys():
                if key in count_s and count_t[key] <= count_s[key]:
                    continue
                else:
                    return False
            return True

        ret = ""
        retLen = 99999999999999
        while l<n and r<=n:
            condition = check(l,r)

            if condition:
                if (retLen > len(s[l:r])):
                    ret = s[l:r]
                    retLen = len(s[l:r])
                l+=1
            else:
                r+=1
        return ret