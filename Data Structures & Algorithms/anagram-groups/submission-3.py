class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            agm = ''.join(sorted(i))
            anagram[agm] = anagram.get(agm,[]) + [i]
        return [i for i in anagram.values()]