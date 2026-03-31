class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = 0
            if c == '.':
                i = self.findChar(curr.children)
                if i==None:
                    return False
            else:
                i = ord(c) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return curr.endOfWord
            
    def findChar(self,children):
        for i in range(len(children)):
            if children[i]:
                return i

        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
    