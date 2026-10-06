class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const freq = new Array(26).fill(0)

        const check = (arr,p) => {
            const sum = arr.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
            if (sum - Math.max(...arr) <= p) return true;
            return false;
        }

        const n = s.length

        let l=0,r=0;
        let window = 0;
        while (l < n) {
            if (r<n && check(freq,k)) {
                freq[s[r].charCodeAt(0) - 'A'.charCodeAt(0)]++
                r++;
                if (check(freq,k))
                window = Math.max(window,r-l)
            } else {
                freq[s[l].charCodeAt(0) - 'A'.charCodeAt(0)]--
                l++;
            }
        }
        return window
    }
}
