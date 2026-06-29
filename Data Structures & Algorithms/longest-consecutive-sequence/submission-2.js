class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const obj = {};
        for (const num of nums) {
            obj[num] = 1;
        }

        const countSeq = (num) => {
            let max = 0;
            while (obj[num]) {
                num++;
                max++;
            }
            return max;
        }

        let ans = 0;

        for (const num of nums) {
            ans = Math.max(ans,countSeq(num));
        }
        
        return ans;
    }
}
