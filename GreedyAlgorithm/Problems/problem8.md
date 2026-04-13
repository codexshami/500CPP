# Problem 8: Minimum Spanning Tree (Prim's)

## Problem Statement
Given a connected, undirected, weighted graph, find the Minimum Spanning Tree (MST) using Prim's algorithm. Return the total weight and the edges of the MST.

## Input Format
- An integer `V` — number of vertices.
- An adjacency list `graph` where `graph[u]` contains `(v, weight)` pairs.

## Output Format
- An integer representing the total weight of the MST.

## Constraints
- 2 <= V <= 10^4
- 1 <= weight <= 10^6

## Example
**Input:** V = 5, graph = {0: [(1,2),(3,6)], 1: [(0,2),(2,3),(3,8),(4,5)], 2: [(1,3),(4,7)], 3: [(0,6),(1,8)], 4: [(1,5),(2,7)]}  
**Output:** 16
