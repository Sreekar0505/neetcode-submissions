class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            visited[s[i]] = visited.get(s[i],0) + 1
            visited[t[i]] = visited.get(t[i],0) - 1
        for j in visited.keys():
            if (visited[j] != 0):
                return False
        return True