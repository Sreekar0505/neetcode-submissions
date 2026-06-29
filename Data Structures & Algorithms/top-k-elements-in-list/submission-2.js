class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {};
        const n = nums.length;

        for (let i=0; i<n; i++) {
            if (!freq[nums[i]]) {
                freq[nums[i]] = 1
            } else {
                freq[nums[i]]++
            }
        }

        const bucket = Array.from({ length: nums.length + 1 }, () => []);

        for (const key of Object.keys(freq)) {
            bucket[freq[key]].push(key)
        }
        console.log(bucket)
        const ans = [];
        let idx = n;
        while (ans.length < k) {
            ans.push(...bucket[idx--]);
        }
        return ans;
    }
}
