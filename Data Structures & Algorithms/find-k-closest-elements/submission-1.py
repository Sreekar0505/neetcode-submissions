class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        curr = 0
        n = len(arr)
        for i in range(k):
            curr += abs(x-arr[i])
        l,r = 0,k
        
        mini = curr
        ans = arr[l:r]
        while r<n:
            curr+=abs(x-arr[r])
            r+=1
            curr-=abs(x-arr[l])
            l+=1
            if curr < mini:
                mini = curr
                ans = arr[l:r]
        return ans