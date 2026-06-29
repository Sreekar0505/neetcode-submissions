class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    missingNumber(nums) {
        let n = nums.length
        const sum = Math.floor(n*(n+1)/2)
        let accured = 0
        for (const num of nums) {
            accured += num
        }
        return sum - accured
    }
}
