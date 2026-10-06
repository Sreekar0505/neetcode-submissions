class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let temp = s.split('')
        let i=0
        let j=temp.length-1

        while (i<j) {
            if (/[^a-zA-Z0-9]/.test(temp[i])) i++;
            else if (/[^a-zA-Z0-9]/.test(temp[j])) j--;
            else if (temp[i].toLowerCase() === temp[j].toLowerCase()) {
                i++;
                j--;
            } else return false
        }
        return true
    }
}
