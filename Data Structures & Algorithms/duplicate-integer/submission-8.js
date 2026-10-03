class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let prev = {}
        for (let i=0; i<nums.length; i++) {
            if (prev.hasOwnProperty(nums[i])){
                return true;
            } else {
                prev[nums[i]] = 1
            }
        }
        return false;
    }
}
