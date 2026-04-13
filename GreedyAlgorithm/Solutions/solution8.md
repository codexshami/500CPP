# Solution 8: Minimum Spanning Tree (Prim's)

## Approach Explanation
Start from any vertex and greedily grow the MST by always picking the minimum-weight edge that connects a visited vertex to an unvisited vertex. Use a min-heap for efficiency.

## Step-by-Step Logic
1. Start from vertex 0. Push all its edges into a min-heap.
2. Mark vertex 0 as visited.
3. Extract the minimum edge. If the destination is unvisited, add the edge weight and push all edges of the new vertex.
4. Repeat until all vertices are visited.

## Complexity
- **Time Complexity:** O(E log V) with a binary heap.
- **Space Complexity:** O(V + E) for the heap and adjacency list.

## Code
```python
import heapq

def prim_mst(V, graph):
    visited = [False] * V
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_weight += weight
        
        for v, w in graph.get(u, []):
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    
    return total_weight
```
