# Solution 7: Minimum Spanning Tree (Kruskal's)

## Approach Explanation
Sort all edges by weight. Use Union-Find (Disjoint Set Union) to greedily add edges that don't form a cycle. Stop when V-1 edges are added.

## Step-by-Step Logic
1. Sort edges by weight in ascending order.
2. Initialize Union-Find with V components.
3. For each edge, if the two vertices are in different components, union them and add the edge weight.
4. Stop when MST has V-1 edges.

## Complexity
- **Time Complexity:** O(E log E) for sorting edges.
- **Space Complexity:** O(V) for Union-Find.

## Code
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal_mst(V, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(V)
    
    mst_weight = 0
    edges_used = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            edges_used += 1
            if edges_used == V - 1:
                break
    
    return mst_weight
```
