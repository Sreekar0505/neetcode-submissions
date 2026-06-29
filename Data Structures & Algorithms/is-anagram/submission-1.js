class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length){
            return false
        }

        const countS = {}, countT = {};

        for (let i=0; i<s.length; i++) {
            countS[s.charAt(i)] = countS.hasOwnProperty(s.charAt(i)) ? countS[s.charAt(i)] + 1 : 1;
            countT[t.charAt(i)] = countT.hasOwnProperty(t.charAt(i)) ? countT[t.charAt(i)] + 1 : 1;
        }

        for (const key in countS) {
            if (countS[key] !== countT[key]){
                return false;
            }
        }

        return true;
    }
}
