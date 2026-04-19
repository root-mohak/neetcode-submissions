

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            pos = s.find('#', i)
            len_str = s[i:pos]
            length = int(len_str)

            word = s[pos + 1 : pos + 1 + length]
            result.append(word)

            i = pos + 1 + length

        return result

