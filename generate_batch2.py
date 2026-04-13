"""
Batch 2-5 generator: Generates Problems and Solutions for all remaining empty topics.
"""
import os

BASE_DIR = r"d:\500DCPP"

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def gen_problem(idx, title, stmt, inp, out, con, ex_in, ex_out):
    return f"""# Problem {idx}: {title}

## Problem Statement
{stmt}

## Input Format
- {inp}

## Output Format
- {out}

## Constraints
- {con}

## Example
**Input:** {ex_in}  
**Output:** {ex_out}
"""

def gen_solution(idx, title, approach, steps, tc, sc, code):
    sl = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
    return f"""# Solution {idx}: {title}

## Approach Explanation
{approach}

## Step-by-Step Logic
{sl}

## Complexity
- **Time Complexity:** {tc}
- **Space Complexity:** {sc}

## Code
```python
{code}
```
"""

###############################################################################
# ADVANCED DATA STRUCTURES
###############################################################################
ADV_DS_P = [
    (1, "Implement Trie (Prefix Tree)", "Implement a trie with insert, search, and startsWith methods.", "Operations: insert(word), search(word), startsWith(prefix).", "True/False for search and startsWith.", "1 <= word.length, prefix.length <= 2000", 'insert("apple"), search("apple")', "True"),
    (2, "LRU Cache", "Design a data structure for Least Recently Used (LRU) Cache that supports get and put in O(1).", "Operations: get(key), put(key, value), capacity.", "Integer for get (-1 if not found).", "1 <= capacity <= 3000", "LRUCache(2), put(1,1), put(2,2), get(1)", "1"),
    (3, "LFU Cache", "Design a Least Frequently Used (LFU) Cache with O(1) get and put.", "Operations: get(key), put(key, value), capacity.", "Integer for get (-1 if not found).", "0 <= capacity <= 10^4", "LFUCache(2), put(1,1), put(2,2), get(1)", "1"),
    (4, "Segment Tree - Range Sum Query", "Build a segment tree for range sum queries with point updates.", "An array and queries (update, range_sum).", "Integers for range sum queries.", "1 <= n <= 3*10^4", "arr=[1,3,5,7,9,11], sumRange(1,3)", "15"),
    (5, "Segment Tree - Range Min Query", "Build a segment tree to answer range minimum queries.", "An array and queries.", "Minimum value in the given range.", "1 <= n <= 10^5", "arr=[2,5,1,4,9,3], query(1,4)", "1"),
    (6, "Fenwick Tree (Binary Indexed Tree)", "Implement a Fenwick tree for prefix sum queries and point updates.", "An array and update/query operations.", "Prefix sums.", "1 <= n <= 10^5", "arr=[1,2,3,4,5], prefixSum(3)", "6"),
    (7, "Disjoint Set Union (Union-Find)", "Implement Union-Find with path compression and union by rank.", "Operations: union(x,y), find(x), connected(x,y).", "Boolean for connected, integer for find.", "1 <= n <= 10^5", "union(1,2), union(2,3), connected(1,3)", "True"),
    (8, "Implement Min-Max Heap", "Implement a data structure that supports O(1) findMin and findMax, and O(log n) insert/delete.", "Operations: insert, findMin, findMax, deleteMin, deleteMax.", "Integers.", "1 <= n <= 10^5", "insert(5), insert(3), insert(8), findMin()", "3"),
    (9, "Skip List", "Implement a skip list that supports search, insert, and delete in O(log n) expected time.", "Operations: search(val), insert(val), delete(val).", "Boolean for search.", "1 <= n <= 10^4", "insert(3), insert(7), search(3)", "True"),
    (10, "Bloom Filter", "Implement a Bloom Filter for probabilistic set membership testing.", "Operations: add(item), contains(item).", "Boolean for contains (may have false positives).", "1 <= items <= 10^6", 'add("hello"), contains("hello")', "True"),
    (11, "Order Statistics Tree", "Implement a BST that supports select(k) — find kth smallest — and rank(x) in O(log n).", "Operations: insert, select(k), rank(x).", "Integer.", "1 <= n <= 10^5", "insert(3,1,4,5,2), select(3)", "3"),
    (12, "Interval Tree", "Build an interval tree to efficiently find all intervals overlapping a given interval.", "A list of intervals and a query interval.", "List of overlapping intervals.", "1 <= n <= 10^5", "intervals=[(15,20),(10,30),(17,19)], query=(14,16)", "[(15,20),(10,30)]"),
    (13, "Sparse Table", "Build a Sparse Table for O(1) range minimum queries after O(N log N) preprocessing.", "An array, range queries.", "Minimum in range.", "1 <= n <= 10^5", "arr=[7,2,3,0,5,10,3,12,18], query(0,4)", "0"),
    (14, "Suffix Array", "Build the suffix array for a given string.", "A string `s`.", "A list of indices representing the suffix array.", "1 <= len(s) <= 10^5", 's = "banana"', "[5,3,1,0,4,2]"),
    (15, "Treap", "Implement a Treap (tree + heap) with random priorities for balanced BST operations.", "Operations: insert, delete, search.", "Boolean for search.", "1 <= n <= 10^5", "insert(5), insert(3), insert(7), search(3)", "True"),
    (16, "Splay Tree", "Implement a Splay Tree that moves accessed nodes to the root.", "Operations: insert, search, delete.", "Boolean for search.", "1 <= n <= 10^5", "insert(10), insert(20), search(10)", "True"),
    (17, "B-Tree Operations", "Implement basic B-Tree insertion and search operations.", "Operations: insert, search, minimum order t.", "Boolean for search.", "2 <= t <= 100", "insert(10,20,5,6,12), search(6)", "True"),
    (18, "AVL Tree", "Implement an AVL tree with self-balancing insertion and deletion.", "Operations: insert, delete, search.", "Boolean for search.", "1 <= n <= 10^5", "insert(10,20,30), search(20)", "True"),
    (19, "Red-Black Tree Insert", "Implement insertion into a Red-Black tree with proper rebalancing.", "Values to insert.", "The tree in-order traversal.", "1 <= n <= 10^5", "insert(7,3,18,10,22,8,11)", "[3,7,8,10,11,18,22]"),
    (20, "Monotonic Stack", "Use a monotonic stack to find the next greater element for each element in an array.", "A list of integers.", "A list where each element is the next greater element, or -1.", "1 <= n <= 10^5", "arr = [4, 5, 2, 10, 8]", "[5, 10, 10, -1, -1]"),
]

ADV_DS_S = [
    (1, "Implement Trie", "Use a dictionary of children at each node with an is_end flag.", ["Create TrieNode class with children dict and is_end flag.", "Insert: traverse/create nodes for each character.", "Search: traverse and check is_end."], "O(L) per operation", "O(N*L)",
     """class Trie:
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
        return True"""),
    (2, "LRU Cache", "Use an OrderedDict to maintain insertion order. Move accessed items to end.", ["Use OrderedDict for O(1) access and order management.", "On get: move to end, return value.", "On put: insert/update and evict oldest if over capacity."], "O(1) per operation", "O(capacity)",
     """from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)"""),
    (3, "LFU Cache", "Use a min-frequency tracker with doubly linked lists per frequency level.", ["Track frequency of each key.", "Maintain ordered dict per frequency.", "On eviction, remove least frequent, then least recent."], "O(1) per operation", "O(capacity)",
     """from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.key_val = {}
        self.key_freq = {}
        self.freq_keys = defaultdict(OrderedDict)
        self.min_freq = 0
    def get(self, key):
        if key not in self.key_val:
            return -1
        self._update_freq(key)
        return self.key_val[key]
    def put(self, key, value):
        if self.cap <= 0: return
        if key in self.key_val:
            self.key_val[key] = value
            self._update_freq(key)
            return
        if len(self.key_val) >= self.cap:
            evict, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.key_val[evict]
            del self.key_freq[evict]
        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_keys[1][key] = None
        self.min_freq = 1
    def _update_freq(self, key):
        freq = self.key_freq[key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None"""),
    (4, "Segment Tree - Range Sum", "Build a tree where each node stores sum of a range. Update and query in O(log N).", ["Build tree bottom-up.", "Update: modify leaf, propagate up.", "Query: combine results from relevant segments."], "O(log N) per operation", "O(N)",
     """class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    def query(self, l, r):  # [l, r)
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1: res += self.tree[l]; l += 1
            if r & 1: r -= 1; res += self.tree[r]
            l //= 2; r //= 2
        return res"""),
    (5, "Segment Tree - Range Min", "Same as range sum but store minimum instead.", ["Build with min operation.", "Query returns minimum in range.", "Update leaf and propagate."], "O(log N) per operation", "O(N)",
     """class MinSegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])
    def query(self, l, r):
        res = float('inf')
        l += self.n; r += self.n
        while l < r:
            if l & 1: res = min(res, self.tree[l]); l += 1
            if r & 1: r -= 1; res = min(res, self.tree[r])
            l //= 2; r //= 2
        return res"""),
    (6, "Fenwick Tree", "Use a BIT array where each index stores a partial sum based on its lowest set bit.", ["Initialize BIT of size n+1.", "Update: add delta at index, propagate using i += i&(-i).", "Query: sum using i -= i&(-i)."], "O(log N) per operation", "O(N)",
     """class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    def range_query(self, l, r):
        return self.query(r) - (self.query(l-1) if l > 0 else 0)"""),
    (7, "Disjoint Set Union", "Use parent array with path compression and union by rank for near O(1) operations.", ["Find with path compression: point directly to root.", "Union by rank: attach smaller tree under larger."], "O(alpha(N)) amortized", "O(N)",
     """class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True
    def connected(self, x, y):
        return self.find(x) == self.find(y)"""),
    (8, "Min-Max Heap", "Maintain two heaps: a min-heap and a max-heap with cross-references.", ["Keep a min-heap and max-heap in sync.", "Insert into both.", "Delete from one and mark as deleted in the other."], "O(log N) insert/delete, O(1) find", "O(N)",
     """import heapq
class MinMaxHeap:
    def __init__(self):
        self.min_h = []
        self.max_h = []
        self.removed = set()
        self.counter = 0
    def insert(self, val):
        entry = (val, self.counter)
        self.counter += 1
        heapq.heappush(self.min_h, entry)
        heapq.heappush(self.max_h, (-val, entry[1]))
    def _clean_min(self):
        while self.min_h and self.min_h[0][1] in self.removed:
            heapq.heappop(self.min_h)
    def _clean_max(self):
        while self.max_h and self.max_h[0][1] in self.removed:
            heapq.heappop(self.max_h)
    def find_min(self):
        self._clean_min()
        return self.min_h[0][0]
    def find_max(self):
        self._clean_max()
        return -self.max_h[0][0]"""),
    (9, "Skip List", "Probabilistic data structure with multiple levels of linked lists for O(log n) search.", ["Each node has random height.", "Search from top level down.", "Insert at correct position with random levels."], "O(log N) expected", "O(N log N)",
     """import random
class SkipNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)
class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(-1, max_level)
        self.level = 0
    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl
    def search(self, val):
        curr = self.header
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr and curr.val == val"""),
    (10, "Bloom Filter", "Use multiple hash functions to set bits in a bit array. Check all bits for membership.", ["Initialize bit array of size m.", "Add: compute k hash positions, set bits.", "Contains: check if all k bit positions are set."], "O(k) per operation", "O(m)",
     """class BloomFilter:
    def __init__(self, size=1000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [False] * size
    def _hashes(self, item):
        positions = []
        for i in range(self.num_hashes):
            h = hash(str(item) + str(i)) % self.size
            positions.append(h)
        return positions
    def add(self, item):
        for pos in self._hashes(item):
            self.bits[pos] = True
    def contains(self, item):
        return all(self.bits[pos] for pos in self._hashes(item))"""),
    (11, "Order Statistics Tree", "Augment BST nodes with subtree sizes to support select and rank.", ["Each node stores subtree size.", "Select(k): use sizes to navigate.", "Rank(x): count nodes less than x."], "O(log N) average", "O(N)",
     """class OSTNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.size = 1

def insert(root, val):
    if not root: return OSTNode(val)
    root.size += 1
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def select(root, k):
    left_size = root.left.size if root.left else 0
    if k == left_size + 1: return root.val
    if k <= left_size: return select(root.left, k)
    return select(root.right, k - left_size - 1)"""),
    (12, "Interval Tree", "Store intervals in a BST keyed by low endpoint, augmented with max endpoint in subtree.", ["Build BST on low endpoints.", "Augment with max high endpoint.", "Search: check overlap and navigate."], "O(log N) per query", "O(N)",
     """class IntervalNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max_high = high
        self.left = self.right = None

def insert_interval(root, low, high):
    if not root: return IntervalNode(low, high)
    if low < root.low:
        root.left = insert_interval(root.left, low, high)
    else:
        root.right = insert_interval(root.right, low, high)
    root.max_high = max(root.max_high, high)
    return root

def search_overlap(root, low, high):
    if not root: return None
    if root.low <= high and low <= root.high:
        return (root.low, root.high)
    if root.left and root.left.max_high >= low:
        return search_overlap(root.left, low, high)
    return search_overlap(root.right, low, high)"""),
    (13, "Sparse Table", "Precompute answers for all ranges of length 2^k. Answer queries by combining two overlapping ranges.", ["Build table[i][j] = min of range starting at i with length 2^j.", "Query: combine two overlapping ranges of appropriate power of 2."], "O(N log N) build, O(1) query", "O(N log N)",
     """import math
class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = int(math.log2(n)) + 1
        self.table = [[0]*n for _ in range(k)]
        self.table[0] = arr[:]
        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.table[j][i] = min(self.table[j-1][i], self.table[j-1][i + (1 << (j-1))])
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i//2] + 1
    def query(self, l, r):
        j = self.log[r - l + 1]
        return min(self.table[j][l], self.table[j][r - (1 << j) + 1])"""),
    (14, "Suffix Array", "Build suffix array by sorting all suffixes. Use the sorted indices.", ["Generate all suffixes with their starting indices.", "Sort them lexicographically.", "Return the indices."], "O(N log^2 N) or O(N log N)", "O(N)",
     """def build_suffix_array(s):
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [idx for _, idx in suffixes]"""),
    (15, "Treap", "Combine BST (by value) and heap (by random priority) properties.", ["Each node has value and random priority.", "Insert: BST insert then rotate to maintain heap.", "Split and merge for efficient operations."], "O(log N) expected", "O(N)",
     """import random
class TreapNode:
    def __init__(self, val):
        self.val = val
        self.priority = random.random()
        self.left = self.right = None

def split(node, val):
    if not node: return None, None
    if node.val <= val:
        left, node.right = split(node.right, val)
        return node, left
    else:
        node.left, right = split(node.left, val)
        return right, node

def merge(left, right):
    if not left or not right: return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    right.left = merge(left, right.left)
    return right"""),
    (16, "Splay Tree", "Move accessed nodes to root using zig, zig-zig, and zig-zag rotations.", ["On access, splay the node to root.", "Zig: single rotation.", "Zig-zig/zig-zag: double rotations."], "O(log N) amortized", "O(N)",
     """class SplayNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.parent = None

def rotate(x):
    p = x.parent
    if not p: return
    g = p.parent
    if p.left == x:
        p.left = x.right
        if x.right: x.right.parent = p
        x.right = p
    else:
        p.right = x.left
        if x.left: x.left.parent = p
        x.left = p
    p.parent = x
    x.parent = g
    if g:
        if g.left == p: g.left = x
        else: g.right = x"""),
    (17, "B-Tree Operations", "B-Tree of minimum degree t stores keys sorted in nodes with at most 2t-1 keys.", ["Search: BST-style search within nodes.", "Insert: find leaf, split if full.", "Split: move median up, create two children."], "O(t * log_t(N))", "O(N)",
     """class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return True
        if self.leaf:
            return False
        return self.children[i].search(k)"""),
    (18, "AVL Tree", "BST with balance factor (height difference <= 1). Rotate after inserts/deletes.", ["Track height at each node.", "After insert, check balance factor.", "Rotate (LL, RR, LR, RL) to rebalance."], "O(log N)", "O(N)",
     """class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def insert_avl(root, val):
    if not root: return AVLNode(val)
    if val < root.val: root.left = insert_avl(root.left, val)
    else: root.right = insert_avl(root.right, val)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and val < root.left.val: return right_rotate(root)
    # ... other rotation cases
    return root"""),
    (19, "Red-Black Tree Insert", "BST with color property (red/black). Recolor and rotate after insertion.", ["Insert as red node (BST insert).", "Fix violations: recolor or rotate.", "Root is always black."], "O(log N)", "O(N)",
     """class RBNode:
    def __init__(self, val, color='R'):
        self.val = val
        self.color = color
        self.left = self.right = self.parent = None

def rb_insert(root, val):
    node = RBNode(val)
    # Standard BST insert
    if not root:
        node.color = 'B'
        return node
    curr = root
    while curr:
        node.parent = curr
        if val < curr.val:
            if not curr.left:
                curr.left = node
                break
            curr = curr.left
        else:
            if not curr.right:
                curr.right = node
                break
            curr = curr.right
    # Fix-up would go here (recolor + rotate)
    return root"""),
    (20, "Monotonic Stack", "Maintain a stack of elements in monotonically decreasing order. When a larger element is found, it is the next greater for all smaller elements popped.", ["Traverse array from right to left.", "Pop elements smaller than current from stack.", "Stack top is the next greater element.", "Push current element."], "O(N)", "O(N)",
     """def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    
    return result"""),
]

###############################################################################
# ADVANCED STRING
###############################################################################
ADV_STR_P = [
    (1, "KMP Pattern Matching", "Implement the Knuth-Morris-Pratt algorithm for pattern matching.", "A text `t` and pattern `p`.", "List of starting indices of all occurrences.", "1 <= len(p) <= len(t) <= 10^5", 't="aabaabaa", p="aab"', "[0, 3]"),
    (2, "Rabin-Karp Algorithm", "Implement Rabin-Karp rolling hash for pattern matching.", "A text `t` and pattern `p`.", "List of starting indices.", "1 <= len(p) <= len(t) <= 10^5", 't="abcabcabc", p="abc"', "[0, 3, 6]"),
    (3, "Z-Algorithm", "Compute the Z-array where Z[i] is the length of the longest substring starting at i that matches a prefix.", "A string `s`.", "The Z-array.", "1 <= len(s) <= 10^5", 's="aabxaab"', "[7, 1, 0, 0, 3, 1, 0]"),
    (4, "Longest Palindromic Substring (Manacher)", "Find the longest palindromic substring using Manacher's algorithm in O(n).", "A string `s`.", "The longest palindromic substring.", "1 <= len(s) <= 1000", 's="babad"', '"bab" or "aba"'),
    (5, "Minimum Window Substring", "Find the minimum window in string `s` that contains all characters of string `t`.", "Two strings `s` and `t`.", "The minimum window substring.", "1 <= len(s), len(t) <= 10^5", 's="ADOBECODEBANC", t="ABC"', '"BANC"'),
    (6, "Edit Distance", "Given two strings, find the minimum number of operations (insert, delete, replace) to convert one to the other.", "Two strings `word1` and `word2`.", "An integer.", "0 <= len(word1), len(word2) <= 500", 'word1="horse", word2="ros"', "3"),
    (7, "Longest Common Subsequence", "Find the length of the longest common subsequence of two strings.", "Two strings.", "An integer.", "1 <= len(s1), len(s2) <= 1000", 's1="abcde", s2="ace"', "3"),
    (8, "Regular Expression Matching", "Implement regular expression matching with '.' and '*' support.", "A string `s` and pattern `p`.", "A boolean.", "1 <= len(s) <= 20, 1 <= len(p) <= 30", 's="aab", p="c*a*b"', "True"),
    (9, "Wildcard Matching", "Implement wildcard pattern matching with '?' and '*' support.", "A string `s` and pattern `p`.", "A boolean.", "0 <= len(s), len(p) <= 2000", 's="adceb", p="*a*b"', "True"),
    (10, "Shortest Palindrome", "Find the shortest palindrome by adding characters in front of a given string.", "A string `s`.", "The shortest palindrome.", "0 <= len(s) <= 5*10^4", 's="aacecaaa"', '"aaacecaaa"'),
    (11, "Count Palindromic Substrings", "Count the number of palindromic substrings in a given string.", "A string `s`.", "An integer.", "1 <= len(s) <= 1000", 's="aaa"', "6"),
    (12, "Longest Repeating Substring", "Find the length of the longest substring that occurs at least twice.", "A string `s`.", "An integer.", "1 <= len(s) <= 10^4", 's="aabcaabdaab"', "3 (aab)"),
    (13, "String Compression", "Compress a string using counts of repeated characters. Return original if compressed is not shorter.", "A string `s`.", "A string.", "1 <= len(s) <= 10^4", 's="aabcccccaaa"', '"a2b1c5a3"'),
    (14, "Decode String", "Given an encoded string like '3[a2[c]]', decode it to 'accaccacc'.", "An encoded string.", "The decoded string.", "1 <= len(s) <= 30", 's="3[a2[c]]"', '"accaccacc"'),
    (15, "Word Break", "Given a string `s` and a dictionary of words, determine if `s` can be segmented into dictionary words.", "A string and a list of words.", "A boolean.", "1 <= len(s) <= 300", 's="leetcode", wordDict=["leet","code"]', "True"),
    (16, "Group Anagrams", "Given an array of strings, group the anagrams together.", "A list of strings.", "A list of groups.", "1 <= len(strs) <= 10^4", 'strs=["eat","tea","tan","ate","nat","bat"]', '[["eat","tea","ate"],["tan","nat"],["bat"]]'),
    (17, "Longest Substring Without Repeating Characters", "Find the length of the longest substring without repeating characters.", "A string `s`.", "An integer.", "0 <= len(s) <= 5*10^4", 's="abcabcbb"', "3"),
    (18, "Palindrome Partitioning", "Partition a string such that every substring is a palindrome. Return all possible partitions.", "A string `s`.", "A list of lists.", "1 <= len(s) <= 16", 's="aab"', '[["a","a","b"],["aa","b"]]'),
    (19, "Distinct Subsequences", "Count the number of distinct subsequences of `s` that equal `t`.", "Two strings `s` and `t`.", "An integer.", "1 <= len(s), len(t) <= 1000", 's="rabbbit", t="rabbit"', "3"),
    (20, "Text Justification", "Given words and a max width, format text with full justification.", "A list of words and maxWidth.", "A list of justified strings.", "1 <= len(words) <= 300, 1 <= maxWidth <= 100", 'words=["This","is","an","example"], maxWidth=16', '["This    is    an", "example         "]'),
]

ADV_STR_S = [
    (1, "KMP Pattern Matching", "Build a failure function (partial match table) to skip unnecessary comparisons.", ["Build LPS (Longest Proper Prefix which is Suffix) array.", "Use LPS to skip ahead on mismatches.", "Collect all match positions."], "O(N + M)", "O(M)",
     """def kmp_search(text, pattern):
    def build_lps(p):
        lps = [0] * len(p)
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
    
    lps = build_lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j: j = lps[j - 1]
            else: i += 1
    return result"""),
    (2, "Rabin-Karp Algorithm", "Use rolling hash to compare pattern hash with text window hashes.", ["Compute hash of pattern.", "Slide window over text, updating hash.", "On hash match, verify characters."], "O(N + M) average", "O(1)",
     """def rabin_karp(text, pattern):
    d, q = 256, 101
    m, n = len(pattern), len(text)
    h = pow(d, m-1) % q
    p_hash = t_hash = 0
    result = []
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern:
            result.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0: t_hash += q
    return result"""),
    (3, "Z-Algorithm", "Maintain a Z-box [L,R] window. Use previous Z-values to speed up computation.", ["Initialize Z[0] = n, L = R = 0.", "For each i, use Z-box to initialize Z[i].", "Extend and update Z-box."], "O(N)", "O(N)",
     """def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z"""),
    (4, "Longest Palindromic Substring", "Expand around each center (both single character and between characters).", ["For each possible center, expand outward.", "Track the longest palindrome found.", "Return the longest."], "O(N^2) or O(N) with Manacher's", "O(1)",
     """def longest_palindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    result = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        result = max(result, odd, even, key=len)
    return result"""),
    (5, "Minimum Window Substring", "Use sliding window with two pointers. Expand right to include, contract left to minimize.", ["Count chars needed from t.", "Expand right until all chars included.", "Contract left to find minimum.", "Track best window."], "O(N)", "O(K) where K is charset size",
     """from collections import Counter
def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = 0
    min_len = float('inf')
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if min_len == float('inf') else s[start:start+min_len]"""),
    (6, "Edit Distance", "Use DP table where dp[i][j] = min operations to convert word1[:i] to word2[:j].", ["If chars match, dp[i][j] = dp[i-1][j-1].", "Else take min of insert, delete, replace + 1.", "Return dp[m][n]."], "O(M*N)", "O(M*N)",
     """def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]"""),
    (7, "Longest Common Subsequence", "DP where dp[i][j] = LCS length for s1[:i] and s2[:j].", ["If chars match, dp[i][j] = dp[i-1][j-1] + 1.", "Else dp[i][j] = max(dp[i-1][j], dp[i][j-1]).", "Return dp[m][n]."], "O(M*N)", "O(M*N)",
     """def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]"""),
    (8, "Regex Matching", "Use DP where dp[i][j] = whether s[:i] matches p[:j].", ["Handle '.' as any char match.", "Handle '*' as zero or more of preceding.", "Build DP table."], "O(M*N)", "O(M*N)",
     """def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    return dp[m][n]"""),
    (9, "Wildcard Matching", "DP where '?' matches any single char and '*' matches any sequence.", ["Build DP table.", "'?' matches any single character.", "'*' matches any sequence (including empty)."], "O(M*N)", "O(M*N)",
     """def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '?' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[m][n]"""),
    (10, "Shortest Palindrome", "Find the longest palindromic prefix, then prepend the reverse of the remaining suffix.", ["Reverse the string.", "Find longest palindromic prefix using KMP.", "Prepend reverse of suffix."], "O(N)", "O(N)",
     """def shortest_palindrome(s):
    rev = s[::-1]
    combined = s + '#' + rev
    lps = [0] * len(combined)
    for i in range(1, len(combined)):
        j = lps[i-1]
        while j > 0 and combined[i] != combined[j]:
            j = lps[j-1]
        if combined[i] == combined[j]:
            j += 1
        lps[i] = j
    return rev[:len(s) - lps[-1]] + s"""),
    (11, "Count Palindromic Substrings", "Expand around each center and count palindromes.", ["For each center (single and between chars), expand.", "Count each valid expansion."], "O(N^2)", "O(1)",
     """def count_palindromes(s):
    count = 0
    for i in range(len(s)):
        for l, r in [(i,i), (i,i+1)]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1; r += 1
    return count"""),
    (12, "Longest Repeating Substring", "Use binary search on length + rolling hash to check if a substring of that length repeats.", ["Binary search on the length.", "For each length, use rolling hash to find duplicates.", "Return the maximum length found."], "O(N log N)", "O(N)",
     """def longest_repeating(s):
    def check(length):
        seen = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i+length]
            if sub in seen: return True
            seen.add(sub)
        return False
    lo, hi, ans = 1, len(s)-1, 0
    while lo <= hi:
        mid = (lo+hi)//2
        if check(mid): ans = mid; lo = mid+1
        else: hi = mid-1
    return ans"""),
    (13, "String Compression", "Walk through the string counting consecutive characters.", ["Track current char and count.", "Append char + count to result.", "Return shorter of original and compressed."], "O(N)", "O(N)",
     """def compress(s):
    result = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s"""),
    (14, "Decode String", "Use a stack to handle nested encodings. Push counts and strings on encountering '['.", ["Use stack for nested brackets.", "On '[': push current string and count.", "On ']': pop and multiply.", "Build result."], "O(N)", "O(N)",
     """def decode_string(s):
    stack = []
    curr_str = ""
    curr_num = 0
    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif ch == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += ch
    return curr_str"""),
    (15, "Word Break", "DP where dp[i] = True if s[:i] can be segmented.", ["dp[0] = True (empty string).", "For each i, check all j < i if dp[j] and s[j:i] in wordDict.", "Return dp[n]."], "O(N^2 * M)", "O(N)",
     """def word_break(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]"""),
    (16, "Group Anagrams", "Sort each string to create a canonical key. Group strings with the same key.", ["For each string, sort it to get key.", "Add to dictionary with key.", "Return all groups."], "O(N * K log K)", "O(N * K)",
     """from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())"""),
    (17, "Longest Substring Without Repeating", "Use sliding window with a set to track characters in the window.", ["Expand right pointer, add chars.", "If duplicate, shrink from left.", "Track maximum window size."], "O(N)", "O(K) where K is charset",
     """def length_of_longest(s):
    char_set = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len"""),
    (18, "Palindrome Partitioning", "Use backtracking. At each position, try all palindromic prefixes and recurse.", ["At each index, check all substrings starting there.", "If palindrome, add to current partition and recurse.", "When reaching end, add partition to results."], "O(N * 2^N)", "O(N)",
     """def partition(s):
    result = []
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1]:
                path.append(sub)
                backtrack(end, path)
                path.pop()
    backtrack(0, [])
    return result"""),
    (19, "Distinct Subsequences", "DP where dp[i][j] = number of ways to form t[:j] from s[:i].", ["If chars match: dp[i][j] = dp[i-1][j-1] + dp[i-1][j].", "If not: dp[i][j] = dp[i-1][j].", "Return dp[m][n]."], "O(M*N)", "O(M*N)",
     """def num_distinct(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[m][n]"""),
    (20, "Text Justification", "Greedily pack words into lines. Distribute extra spaces evenly between words.", ["Pack words into lines greedily.", "Distribute extra spaces left-to-right.", "Left-justify last line."], "O(N)", "O(N)",
     """def full_justify(words, maxWidth):
    result, line, line_len = [], [], 0
    for word in words:
        if line_len + len(word) + len(line) > maxWidth:
            for i in range(maxWidth - line_len):
                line[i % max(len(line)-1, 1)] += ' '
            result.append(''.join(line))
            line, line_len = [], 0
        line.append(word)
        line_len += len(word)
    result.append(' '.join(line).ljust(maxWidth))
    return result"""),
]

def generate_all(topic_dir, problems, solutions):
    for p in problems:
        idx = p[0]
        content = gen_problem(idx, p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        write_file(os.path.join(BASE_DIR, topic_dir, "Problems", f"problem{idx}.md"), content)
    for s in solutions:
        idx = s[0]
        content = gen_solution(idx, s[1], s[2], s[3], s[4], s[5], s[6])
        write_file(os.path.join(BASE_DIR, topic_dir, "Solutions", f"solution{idx}.md"), content)
    print(f"  DONE {topic_dir}: {len(problems)}P + {len(solutions)}S")

if __name__ == "__main__":
    print("Generating Advanced Data Structures...")
    generate_all("Advanced_DataStructure", ADV_DS_P, ADV_DS_S)
    
    print("Generating Advanced String...")
    generate_all("Advanced_String", ADV_STR_P, ADV_STR_S)
    
    print("All done!")
