class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        n=len(people)
        people.sort()
        l,r = 0,n-1
        while r>=0 and people[r]+people[l] > limit:
            r-=1
            count+=1
        while l<=r:
            count+=1
            r-=1
            l+=1
        return count
