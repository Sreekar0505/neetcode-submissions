class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_visited = {}
        t_visited = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            s_visited[s[i]] = s_visited.get(s[i],0) + 1
            t_visited[t[i]] = t_visited.get(t[i],0) + 1
        return s_visited == t_visited