class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const count = {}
        for (let i=0; i<nums.length; i++) {
            if (count.hasOwnProperty(nums[i])) {
                return true;
            } else {
                count[nums[i]] = 1
            }
        }
        return false
    }
}
