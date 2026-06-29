class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def createPar(ans,curr,left,right):
            if len(curr) == 2*n and left == right:
                ans.append(curr)
            else:
                if left+right < 2*n:
                    createPar(ans,curr+'(',left+1,right)
                    if right < left:
                        createPar(ans,curr+')',left,right+1)
        createPar(ret,"",0,0)

        return ret