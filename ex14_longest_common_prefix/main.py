def get_len_common_prefix(strs: List[str]) -> int:
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if i >= len(s) or s[i] != strs[0][i]:
                return i
        
        i += 1
    return len(strs[0])
            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        return strs[0][:get_len_common_prefix(strs)]
