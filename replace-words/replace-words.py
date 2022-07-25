class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
    
    def search(self,word):
        curr = self.root
        currWord = ''
        for c in word:
            if c not in curr.children: return word
            currWord += c
            curr = curr.children[c]
            if curr.word: return currWord 
        
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        newSentence = []
        for word in sentence.split(' '):
            newSentence.append(trie.search(word))
        
        return ' '.join(newSentence)