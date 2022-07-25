class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.sum = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = defaultdict(int)

    
    def insert(self, key: str, val: int) -> None:
        diff = val - self.map[key]
        curr = self.root
        for c in key:
            curr = curr.children[c]
            curr.sum += diff
        self.map[key] = val
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        
        for c in prefix:
            if c not in curr.children: return 0
            curr = curr.children[c]
    
        return curr.sum
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)