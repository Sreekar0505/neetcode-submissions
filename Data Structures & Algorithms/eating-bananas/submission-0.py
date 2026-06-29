class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(val):
            ret = 0
            for i in piles:
                ret += (i//val)
                if i%val:
                    ret += 1
            if ret <= h:
                return True
            else:
                return False
        
        l,r = 1, max(piles)

        while l<r:
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l