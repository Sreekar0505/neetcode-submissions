class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const visited = {};

        for (const elm of nums) {
            if (visited.hasOwnProperty(elm)) {
                return true
            }
            visited[elm] = 1
        }
        return false
    }
}
