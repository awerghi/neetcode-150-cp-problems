from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0 : return ""
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "" : return []
        # the most important symbol is the first one, it gives us how we will proceed all over the string
        res_list = []

        while s != '':
            diez_index = s.index("#")
            len_partition = int(s[:diez_index])
            partition = s[diez_index+1:diez_index+1+len_partition]
            res_list.append(partition)
            s = s[diez_index+1+len_partition:]
        return res_list



s = Solution()
print(s.encode (["we","say",":","yes"])) # -> output : 2#we3#say1#:3#yes
print(s.decode("2#we3#say1#:3#yes"))     # -> output  : ['we', 'say', ':', 'yes']