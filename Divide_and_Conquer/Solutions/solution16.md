# Solution 16: Construct Binary Tree from Preorder and Inorder

## Approach Explanation
First element of preorder is the root. Find it in inorder to determine left and right subtrees. Recursively build left and right subtrees.

## Step-by-Step Logic
1. Root = preorder[0].
2. Find root's index in inorder → determines left and right subtree sizes.
3. Recursively build left subtree from corresponding preorder and inorder slices.
4. Recursively build right subtree similarly.

## Complexity
- **Time Complexity:** O(N) with hash map for inorder indices.
- **Space Complexity:** O(N).

## Code
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = [0]
    
    def helper(in_left, in_right):
        if in_left > in_right:
            return None
        
        root_val = preorder[pre_idx[0]]
        pre_idx[0] += 1
        root = TreeNode(root_val)
        
        mid = inorder_map[root_val]
        root.left = helper(in_left, mid - 1)
        root.right = helper(mid + 1, in_right)
        
        return root
    
    return helper(0, len(inorder) - 1)
```
