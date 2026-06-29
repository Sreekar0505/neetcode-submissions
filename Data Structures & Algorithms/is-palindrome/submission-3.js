class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let inp = ''
        for (let i=0; i<s.length; i++) {
            if (/^[a-zA-Z0-9]$/.test(s[i])) {
                inp += s[i].toLowerCase()
            }
        }

        for (let i=0; i<Math.floor(inp.length/2); i++) {
            if (inp[i] !== inp[inp.length-1-i]) return false
        }
        return true
    }
}
