class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const mp = {}

        let l=0, res=0;

        for (let r=0; r<s.length; r++) {
            if (mp.hasOwnProperty(s[r])) {
                l = Math.max(mp[s[r]] + 1,l)
            }
            mp[s[r]] = r
            res = Math.max(res, r-l+1)
        }
        return res
    }
}
