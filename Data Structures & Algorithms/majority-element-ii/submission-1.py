class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        elm1 = -1
        elm2 = -1
        for i in nums:
            if elm2 != i and count1 == 0:
                elm1 = i
                count1 = 1
            elif elm1 != i and count2 == 0:
                elm2 = i
                count2 = 1
            elif i == elm1:
                count1+=1
            elif i == elm2:
                count2+=1
            else:
                count1-=1
                count2-=1
        cnt1, cnt2 = 0,0

        for i in nums:
            if i == elm1:
                cnt1+=1
            if i == elm2:
                cnt2+=1
        ans = []
        if cnt1 > len(nums)//3:
            ans.append(elm1)
        if cnt2 > len(nums)//3:
            ans.append(elm2)
        return ans

