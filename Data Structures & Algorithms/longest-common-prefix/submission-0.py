class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        count =''
        for i in range(len(first)):
            if first[i]!=last[i]:
                return count
            count+=first[i]
        return count

        