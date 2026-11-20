class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.letters: Dict[str, TreeNode] = {}

class PrefixTree:

    def __init__(self):
        self.top = TreeNode(0)
        
    def insert(self, word: str) -> None:
        curr = self.top
        for c in word:
            if c not in curr.letters:
                curr.letters[c] = TreeNode(0)
            curr = curr.letters[c]
        curr.val = 1

    def search(self, word: str) -> bool:
        curr = self.top
        for c in word:
            if c not in curr.letters:
                return False
            curr = curr.letters[c]
        
        return curr.val == 1

    def startsWith(self, prefix: str) -> bool:
        curr = self.top
        for c in prefix:
            if c not in curr.letters:
                return False
            curr = curr.letters[c]
        
        return True
        