# Solution 3: Huffman Coding

## Approach Explanation
Use a min-heap (priority queue) to repeatedly extract the two nodes with lowest frequency, merge them into a new node, and insert back. Build the tree bottom-up and derive codes by traversing left (0) and right (1).

## Step-by-Step Logic
1. Create a leaf node for each character and push into a min-heap.
2. While heap has more than one node: extract two minimum nodes, create a parent with freq = sum, push back.
3. Traverse the tree to assign binary codes (left=0, right=1).

## Complexity
- **Time Complexity:** O(N log N) where N is the number of unique characters.
- **Space Complexity:** O(N) for the tree.

## Code
```python
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(freq):
    heap = [HuffmanNode(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    # Generate codes
    codes = {}
    def generate_codes(node, code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
            return
        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")
    
    generate_codes(heap[0])
    return codes
```
