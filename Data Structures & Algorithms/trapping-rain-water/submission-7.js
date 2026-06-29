class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        const n = height.length
        const prev = Array(n).fill(0)
        const post = Array(n).fill(0)

        for (let i=1; i<n; i++) {
            prev[i] = Math.max(height[i-1], prev[i-1])
        }


        for (let i=n-2; i>=0; i--) {
            post[i] = Math.max(height[i+1], post[i+1])
        }

        let ans = 0

        for (let i=0; i<n; i++) {
            const store = Math.min(prev[i], post[i]) - height[i]
            ans += store > 0 ? store : 0
        }

        return ans
    }
}
