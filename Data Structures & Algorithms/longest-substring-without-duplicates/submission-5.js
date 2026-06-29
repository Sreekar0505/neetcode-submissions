class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const dic = {}

        let l=0, res=0;

        for (let r=0; r<s.length; r++) {
            if (dic.hasOwnProperty(s[r])) {
                l = Math.max(dic[s[r]]+1,l)
            }
            dic[s[r]] = r
            res = Math.max(res, r-l+1)
        }

        return res;
    }
}
