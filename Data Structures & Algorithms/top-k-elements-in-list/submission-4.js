class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {}
        for (let i=0; i<nums.length; i++) {
            if (Object.hasOwn(freq, nums[i])) {
                freq[nums[i]]++;
            } else {
                freq[nums[i]]=1;
            }
        }

        const temp = Array.from(Object.entries(freq)).sort((a,b) => b[1] - a[1]);

        return Array.from(temp.slice(0,k), x => Number(x[0]))
    }
}
