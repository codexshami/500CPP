# Solution 1: Implement Trie

## Approach Explanation
Use a dictionary of children at each node with an is_end flag.

## Step-by-Step Logic
1. Create TrieNode class with children dict and is_end flag.
2. Insert: traverse/create nodes for each character.
3. Search: traverse and check is_end.

## Complexity
- **Time Complexity:** O(L) per operation
- **Space Complexity:** O(N*L)

## Code
```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True
    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    def startsWith(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```
