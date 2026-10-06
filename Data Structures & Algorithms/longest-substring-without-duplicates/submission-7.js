class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let res = 0;
        if (s.length == 0) return res;
        const n = s.length;
        const freq = {};

        let l=0, r=0;

        while (l<n) {
            if (!Object.hasOwn(freq,s[r]) || freq[s[r]] === 0){
                freq[s[r]] = 1;
                if (r<n) {
                    r++;
                    res = Math.max(res,r-l)
                } else return res;
            } else {
                freq[s[l]]--;
                l++
            }
        }


        return res;
    }
}
