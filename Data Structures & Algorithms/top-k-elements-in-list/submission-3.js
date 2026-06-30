class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {}
        const n = nums.length
        const freq = Array.from({ length: nums.length + 1 }, () => []);

        for (let i=0; i<n; i++) {
            if (Object.hasOwn(count,nums[i])) {
                count[nums[i]]++
            } else {
                count[nums[i]] = 1
            }
        }

        for (const [num, cnt] of Object.entries(count)) {
            if (!freq[cnt]) freq[cnt] = [];
            freq[cnt].push(Number(num)); // Object keys become strings in JS, cast back if needed
        }
        const ans = [];

        for (let i=freq.length-1; i>0; i--) {
            for (let j=0; j<freq[i].length; j++){
                if (k===0) {
                    return ans
                }
                ans.push(freq[i][j])
                k-=1
            }
        }

        return ans
    }
}
