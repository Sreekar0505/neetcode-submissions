class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0, r = s.length-1

        while (l<r) {
            if (this.isAlphaNum(s[l]) && this.isAlphaNum(s[r])) {
                if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                    return false;
                }
                l++;
                r--;
            } else if (!this.isAlphaNum(s[r])) {
                r--;
            } else {
                l++;
            }
        }
        return true;
    }

    isAlphaNum(a) {
        return (a >= 'A' && a <= 'Z' ||
                a >= 'a' && a <= 'z' ||
                a >= '0' && a <= '9');
    }
}
