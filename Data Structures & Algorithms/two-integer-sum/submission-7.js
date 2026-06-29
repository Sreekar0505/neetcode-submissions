class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let visited = {}
        for (let i=0; i<nums.length; i++) {
            if (Object.hasOwn(visited, target-nums[i])) {
                return [visited[target-nums[i]], i]
            }
            visited[nums[i]] = i
        }
        return [-1,-1]
    }
}
