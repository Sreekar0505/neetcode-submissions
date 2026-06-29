class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l=0, r=s.length-1

        while (l<r) {
            if (this.isAlphaNumeric(s[l]) && this.isAlphaNumeric(s[r])) {
                if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                    return false;
                }
                l++;
                r--;
            } else if (!this.isAlphaNumeric(s[l])) l++
            else r--
        }
        return true
    }

    isAlphaNumeric(a) {
        return /^[A-Za-z0-9]$/.test(a)
    }
}
