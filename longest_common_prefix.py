from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_counts = [len(elt) for elt in strs]
        res_str = ""
        i = 0
        while i < min(len_counts):
            str_elts = [elt[i] for elt in strs]
            if len(set(str_elts)) > 1 :
                break
            else :
                res_str += str_elts[0]
            i += 1
        return res_str
