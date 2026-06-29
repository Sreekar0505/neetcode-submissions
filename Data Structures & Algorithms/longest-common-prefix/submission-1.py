class Solution:
    def sbstr(self, str1, str2):
        ans = ""
        for i in range(min(len(str1),len(str2))):
            if (str1[i] == str2[i]):
                ans += str1[i]
            else:
                break
        return ans
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        ans = strs[0]
        for elm in strs:
            ans = self.sbstr(ans,elm)
        return ans