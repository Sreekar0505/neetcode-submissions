class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)

        if n<m:
            nums1 , nums2 = nums2, nums1
            m,n = n,m

        l,r = 0,m

        while l<=r:
            partX = (l+r)//2
            partY = (m+n+1)//2 - partX

            leftTop,leftBottom = float('-inf'),float('-inf')
            rightTop,rightBottom = float('inf'),float('inf')

            if partX-1 >= 0:
                leftTop = nums1[partX-1]
            if partX < m:
                rightTop = nums1[partX]
            if partY-1 >= 0:
                leftBottom = nums2[partY-1]
            if partY < n:
                rightBottom = nums2[partY]
            
            if leftTop <= rightBottom and leftBottom <= rightTop:
                if (m+n)%2 == 0:
                    return (max(leftTop,leftBottom)+min(rightTop,rightBottom))/2
                else:
                    return max(leftTop,leftBottom)
            elif leftTop > rightBottom:
                r = partX-1
            else:
                l = partX+1

        return 0









