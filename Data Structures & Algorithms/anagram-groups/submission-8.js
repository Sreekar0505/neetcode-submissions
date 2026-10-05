class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const dict = {}

        for (let i=0; i<strs.length; i++) {
            const temp = strs[i].split('').sort().join('');
            if (Object.hasOwn(dict, temp)) {
                dict[temp].push(strs[i])
            } else {
                dict[temp] = [strs[i]]
            }
        }

        return Object.values(dict)
    }
}
