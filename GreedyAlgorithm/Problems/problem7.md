# Problem 7: Minimum Spanning Tree (Kruskal's)

## Problem Statement
Given a connected, undirected, weighted graph, find the Minimum Spanning Tree (MST) using Kruskal's algorithm. Return the total weight of the MST.

## Input Format
- An integer `V` — number of vertices.
- A list of tuples `edges` where each tuple `(u, v, weight)` represents an edge.

## Output Format
- An integer representing the total weight of the MST.

## Constraints
- 2 <= V <= 10^4
- 1 <= E <= V*(V-1)/2
- 1 <= weight <= 10^6

## Example
**Input:** V = 4, edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]  
**Output:** 19  
**Explanation:** MST includes edges (2,3,4), (0,3,5), (0,1,10).
