class Solution {
    check(map1, map2) {
        for (const key in map2) {
            if (map2[key] !== 0 && map1[key] !== map2[key]) return false
        }
        return true
    }
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length > s2.length) return false
        const mp1 = {}, mp2 = {}
        for (let i=0; i<s1.length; i++) {
            mp1[s1[i]] = 1 + (mp1[s1[i]] | 0)
            mp2[s2[i]] = 1 + (mp2[s2[i]] | 0)
        }

        
        let l=0
        for (let r=s1.length; r<=s2.length; r++) {
            if (this.check(mp1,mp2)) return true
            mp2[s2[r]] = 1 + (mp2[s2[r]] | 0)
            mp2[s2[l]]--;
            l++;
        }
        return false
    }
}
