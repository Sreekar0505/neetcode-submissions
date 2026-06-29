class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        if (t === '') return ''

        const countT={}, window={}

        for (let i=0; i<t.length; i++) {
            countT[t[i]] = 1 + (countT[t[i]] | 0)
        }

        let have=0, need=Object.keys(countT).length
        let res = [-1,-1], resLen = Number.POSITIVE_INFINITY
        let l=0
        for (let r=0; r<s.length; r++) {
            let char = s[r]
            window[char] = 1 + (window[char] | 0)
            if (char in countT && window[char] === countT[char]) {
                have++
            }
            while (have === need) {
                if (r-l+1 < resLen) {
                    res = [l,r]
                    resLen = (r-l+1)
                } 
                window[s[l]]--
                if (s[l] in countT && window[s[l]] < countT[s[l]]) {
                    have--
                }
                l++
            }
        }
        return resLen < Number.POSITIVE_INFINITY ? s.substring(res[0],res[1]+1) : ''
    }
}
