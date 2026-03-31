from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            mem[key].append(word)
        return [value for value in mem.values()]


        list_of_dicts = []
        res = []
        
        for word in strs:
            mem = {}
            for letter in word:
                mem[letter] = mem.get(letter,0)+1
            list_of_dicts.append(mem)
        visited = []
        for i in range(len(list_of_dicts)):
            if strs[i] in visited:
                continue
            curr_anagram=[strs[i]]
            for j in range(i+1,len(list_of_dicts)):
                if list_of_dicts[i]==list_of_dicts[j]:
                    curr_anagram.append(strs[j])
                    visited.append(strs[j])
            res.append(curr_anagram)
        return res



                

        