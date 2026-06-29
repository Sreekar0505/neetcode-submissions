class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const n = height.length
        const maxLeft = Array(n).fill(0)
        const maxRight = Array(n).fill(0)

        for (let i=1; i<n; i++) {
            maxLeft[i] = Math.max(maxLeft[i-1],height[i-1])
            maxRight[n-1-i] = Math.max(maxRight[n-i],height[n-i])
        }

        let ans = 0;

        for (let i=0; i<n; i++) {
            const store = Math.min(maxLeft[i],maxRight[i]) - height[i]
            ans += store > 0 ? store : 0;
        }

        return ans;
    }
}
