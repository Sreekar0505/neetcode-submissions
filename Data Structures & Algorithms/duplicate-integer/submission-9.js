class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let visited = {}

        for (let num of nums) {
            if (Object.hasOwn(visited,num)) {
                return true;
            }
            visited[num] = 1
        }
        return false
    }
}
