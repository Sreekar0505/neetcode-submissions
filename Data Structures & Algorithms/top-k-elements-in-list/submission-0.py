class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        count = {}
        freq = [[] for n in range(n+1)]

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for key, val in count.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for elm in freq[i]:
                ans.append(elm)
                if (len(ans) == k):
                    return ans
        return []