class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        n = len(s)
        l,r = 0,0

        ret = 0
        while l<n and r<n:
            count[s[r]] = count.get(s[r],0) + 1
            while l<n and (r+1-l - max(count.values()))>k:
                count[s[l]] -= 1
                l+=1
            ret = max(ret,r+1-l)
            r+=1
        return ret
                
