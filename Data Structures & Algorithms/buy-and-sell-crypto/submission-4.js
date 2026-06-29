class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let min = prices[0]
        let ans = 0
        for (let i=0; i<prices.length; i++) {
            min = Math.min(min,prices[i])
            ans = Math.max(prices[i] - min, ans)
        }
        return ans
    }
}
