class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}
        for i in strs:
            ana = str(sorted(list(i)))
            if ana in visited:
                visited[ana].append(i)
            else:
                visited[ana] = [i]
        return visited.values()