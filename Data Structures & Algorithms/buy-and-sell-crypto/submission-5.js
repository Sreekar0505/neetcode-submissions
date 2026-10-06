class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        const n = prices.length;
        const prev = new Array(n).fill(0)
        const next = new Array(n).fill(0)

        prev[0] = prices[0]
        next[n-1] = prices[n-1]

        for (let i=1; i<n; i++) {
            prev[i] = Math.min(prev[i-1],prices[i])
        }
        for (let j=n-2;j>=0;j--) {
            next[j] = Math.max(next[j+1],prices[j])
        }
        
        let res = 0;
        for (let i=0; i<n; i++) {
            res = Math.max(next[i]-prev[i],res)
        }

        return res;
    }
}
