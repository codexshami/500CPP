# Solution 17: File System

## Approach Explanation
Directory contains files and subdirectories. Support path-based operations.

## Step-by-Step Logic
1. File has name and content.
2. Directory has children dict.
3. Traverse path to find target.

## Complexity
- **Time Complexity:** O(P) where P is path depth
- **Space Complexity:** O(N)

## Code
```python
class FileNode:
    def __init__(self, name, is_dir=True):
        self.name = name
        self.is_dir = is_dir
        self.children = {} if is_dir else None
        self.content = '' if not is_dir else None

class FileSystem:
    def __init__(self): self.root = FileNode('/')
    def _traverse(self, path):
        node = self.root
        for part in path.strip('/').split('/'):
            if part: node = node.children.get(part)
            if not node: return None
        return node
    def mkdir(self, path):
        node = self.root
        for part in path.strip('/').split('/'):
            if part not in node.children:
                node.children[part] = FileNode(part)
            node = node.children[part]
```
