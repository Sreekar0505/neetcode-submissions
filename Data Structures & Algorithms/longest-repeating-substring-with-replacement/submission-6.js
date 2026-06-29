class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const count={}
        let res=0

        let l=0
        let maxf=0

        for (let r=0; r<s.length; r++) {
            count[s[r]] = 1 + (count[s[r]] | 0)
            maxf = Math.max(maxf, count[s[r]])
            while ((r-l+1) - maxf > k) {
                count[s[l]]-=1
                l+=1
            }
            res = Math.max(res, r-l+1)
        }
        return res
    }
}
