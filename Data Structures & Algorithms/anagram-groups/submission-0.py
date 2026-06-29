class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        def constructHash(string):
            count = [0] * 26
            for char in string:
                count[ord(char)-ord('a')] += 1
 
            return tuple(count)

        for elm in strs:
            newHash = constructHash(elm)
            if newHash not in anaDict:
                anaDict[newHash] = []
            anaDict[newHash].append(elm)


        return anaDict.values() 