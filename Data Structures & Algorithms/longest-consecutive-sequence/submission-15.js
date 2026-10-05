class Solution {
    /**
     * @param {number[]}
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0;
        const mp = new Set(nums);
        let ans = 1;
        for (const num of mp) {
            if (!mp.has(num - 1)) {
                let curr = num;
                while (mp.has(curr)) {
                    curr++;
                }
                ans = Math.max(ans, curr - num);
            }
        }

        return ans;
    }
}
