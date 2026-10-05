class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const n = nums.length;
        if (n===0) return 0;
        const set = new Set(nums);
        
        let max = 1;

        for (const num of nums) {
            if (!set.has(num-1)) {
                let curr = num;
                while (set.has(curr)){
                    curr++;
                }
                max = Math.max(max,curr-num);
            }
        }
        return max;
    }
}
