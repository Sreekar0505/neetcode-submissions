class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a, b) => a - b)
        const ans=[]
        for (let x=0; x<nums.length-2; x++) {
            if (nums[x] > 0) break;
            if (x>0 && nums[x] === nums[x-1]) continue;
            let l = x+1, r = nums.length-1
            while (l<r) {
                if (nums[x] + nums[l] + nums[r] === 0){
                    ans.push([nums[x],nums[l],nums[r]])
                    l++;
                    r--;
                    while (l<r && nums[l] === nums[l-1]) {
                        l++;
                    }
                } else if (nums[x] + nums[l] + nums[r] > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return ans;
    }
}
