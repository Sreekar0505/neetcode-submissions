class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        const isSame = (a,b) => a.length === b.length && a.every((val, i) => val === b[i])
        let visited_s = []; 
        let visited_t = [];
        for (let i=0; i<26; i++) {
            visited_s.push(0);
            visited_t.push(0);
        }
        for (let i=0; i<s.length; i++) {
            visited_s[s[i].charCodeAt(0) - 'a'.charCodeAt(0)]++
            visited_t[t[i].charCodeAt(0) - 'a'.charCodeAt(0)]++
        }
        return isSame(visited_s, visited_t)
    }
}
