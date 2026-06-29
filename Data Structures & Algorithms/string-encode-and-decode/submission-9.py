class Solution:

    def encode(self, strs: List[str]) -> str:
        return '-$#%-='.join(strs) + '#' + str(len(strs))

    def decode(self, s: str) -> List[str]:
        length = ''

        while (s[-1] != '#'):
            length = s[-1] + length
            s = s[:-1]
        
        s = s[:-1]

        if int(length) == 0:
            return []
        return list(s.split('-$#%-='))