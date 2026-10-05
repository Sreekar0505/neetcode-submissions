class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {};

        for (let num of nums) {
            if (Object.hasOwn(freq, num)) {
                freq[num]++
            } else {
                freq[num] = 1
            }
        }

        const arr = new Array(nums.length+1)

        for (let [key,value] of Object.entries(freq)) {
            if (arr[value] !== undefined) {
                arr[value].push(key)
            } else {
                arr[value] = [key]
            }
        }

        const res = []
        for (let i=nums.length+1; i>0; i--) {
            if (k<=0) return res;
            if (arr[i] === undefined) continue;
            res.push(...arr[i])
            k=k-arr[i].length
        }

        return res
    }
}
