class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        const ans = Array(n).fill(1);

        let temp = 1;
        for (let i=0; i<n-1; i++) {
            temp *= nums[i];
            ans[i+1] *= temp;
        }

        temp = 1
        for (let i=n-1; i>0; i--) {
            temp *= nums[i];
            ans[i-1] *= temp;
        }

        return ans;
    }
}
