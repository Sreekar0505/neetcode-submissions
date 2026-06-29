class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const count = {}

        let l=0, max=0, res=0;

        for (let r=0; r<s.length; r++) {
            count[s[r]] = 1 + (count[s[r]] | 0)
            max = Math.max(max, count[s[r]])
            while (r-l+1 - max > k) {
                count[s[l]]--;
                l++;
            }
            res = Math.max(res, r-l+1)
        }
        return res
    }
}
