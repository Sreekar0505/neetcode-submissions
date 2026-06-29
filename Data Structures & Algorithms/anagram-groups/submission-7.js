class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let ans = {}
        for (let i=0; i<strs.length; i++) {
            if (Object.hasOwn(ans,[...strs[i]].sort().join(''))){
                ans[[...strs[i]].sort().join('')].push(strs[i])
            }
            else {
                ans[[...strs[i]].sort().join('')] = [strs[i]]
            }
        }
        return Object.values(ans)
    }
}
