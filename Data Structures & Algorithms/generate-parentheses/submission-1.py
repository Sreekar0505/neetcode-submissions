class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def backtrack(left,right,val):
            if left == right == n:
                ret.append(val)
                return
            
            if left < n:
                backtrack(left+1,right,val+'(')
            if right < left:
                backtrack(left,right+1,val+')')
        
        backtrack(0,0,'')
        return ret