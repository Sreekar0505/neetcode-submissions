class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = 1
        def countSeq(num):
            ret = 0
            while dic.get(num,0) == 1:
                ret+=1
                num+=1
            return ret

        maxi = 0

        for i in nums:
            maxi = max(maxi,countSeq(i))
        
        return maxi