class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {}
        for (let num of nums) {
            let temp = freq[num] || 0
            freq[num] = temp + 1
        }

        let arr = new Array(nums.length)
        for (let [key,val] of Object.entries(freq)) {
            if (arr[val]){
                arr[val].push(Number(key))
            } else {
                arr[val] = [Number(key)]
            }
        }

        let ans = []
        for (let i = arr.length-1; i >= 0; i--) {
            if (ans.length === k) return ans

            if (!arr[i]) continue
            ans.push(...arr[i])
        }

        return ans
    }
}
