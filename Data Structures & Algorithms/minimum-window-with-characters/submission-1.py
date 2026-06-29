class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0

        n = len(s)

        count_t,window = {}, {}

        for i in t:
            count_t[i] = count_t.get(i,0) + 1

        def check(l,r):
            for key in count_t.keys():
                if key in window and count_t[key] <= window[key]:
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
                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                    window[s[l]] -= 1
                l+=1
            else:
                r+=1
                if r-1 < n:
                    window[s[r-1]] = window.get(s[r-1],0) + 1
        return ret