class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        const left = Array(n).fill(1)
        const right = Array(n).fill(1)

        for (let i=1; i<n; i++) {
            left[i] = left[i-1] * nums[i-1]
        }

        for (let i=n-2; i>=0; i--) {
            right[i] = right[i+1] * nums[i+1]
        }

        return nums.map((_, idx) => {
            return left[idx] * right[idx];
        })
    }
}
