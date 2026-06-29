class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        n = len(s)
        if (n == 0): return 0
        ret = 0
        dic = {}
        while l<n and r<n:
            dic[s[r]] = dic.get(s[r],0) + 1
            while l<n and dic[s[r]] > 1:
                dic[s[l]] -= 1
                l+=1
            ret = max(ret,r-l+1)
            r+=1
        return ret