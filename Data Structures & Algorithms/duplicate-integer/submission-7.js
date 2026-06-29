class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let visited = {}
        for (let i=0; i<nums.length; i++) {
            if (Object.hasOwn(visited,nums[i])) {
                return true
            }
            visited[nums[i]] = 1
        }
        return false
    }
}
