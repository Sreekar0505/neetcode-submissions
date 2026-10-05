class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let n = nums.length;
        let prev = new Array(n);
        let next = new Array(n);
        prev[0] = 1
        next[n-1] = 1
        for (let i=1; i<n; i++) {
            prev[i] = prev[i-1] * nums[i-1]
            next[n-1-i] = next[n-i] * nums[n-i]
        }

        for (let i=0; i<n; i++) {
            nums[i] = prev[i] * next[i]
        }

        return nums;
    }
}
