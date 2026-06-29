def commonPrefix(str1, str2):
    ret = ""
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            ret+=str1[i]
        else:
            break
    return ret

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in strs:
            common = commonPrefix(common,i)
        return common