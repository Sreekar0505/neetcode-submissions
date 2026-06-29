class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0
        const mp = {}
        for (let i=0; i<nums.length; i++) {
            mp[nums[i]] = 1
        }
        let ans = 1;
        for (const num of nums) {
            if (mp.hasOwnProperty(num-1)) {
                let curr = num
                while (mp.hasOwnProperty(curr)) {
                    curr++;
                }
                ans = Math.max(ans, curr-num+1);
            }
        }

        return ans
    }
}
