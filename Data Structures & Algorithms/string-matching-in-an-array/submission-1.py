class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for word in words:
            for w in words:
                if w == word:
                    continue
                if word in w:
                    res.add(word)
        return [word for word in res]
        