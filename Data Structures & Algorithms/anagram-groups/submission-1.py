class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        for elm in strs:
            count = [0] * 26
            for char in elm:
                count[ord(char)-ord('a')] += 1

            newHash = tuple(count)

            if newHash not in anaDict:
                anaDict[newHash] = []

            anaDict[newHash].append(elm)

        return anaDict.values() 