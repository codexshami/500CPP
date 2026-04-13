# Solution 7: Strassen's Matrix Multiplication

## Approach Explanation
Split each n×n matrix into four n/2×n/2 submatrices. Compute 7 products (instead of 8) using clever additions/subtractions, then combine.

## Step-by-Step Logic
1. Base case: 1×1 matrices — multiply directly.
2. Split A and B into quadrants.
3. Compute 7 Strassen products (M1..M7).
4. Combine to form result quadrants.

## Complexity
- **Time Complexity:** O(N^2.807).
- **Space Complexity:** O(N^2).

## Code
```python
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2
    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)
    
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))
    
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)
    
    return combine(C11, C12, C21, C22)

def split(M):
    n = len(M)
    mid = n // 2
    top_left = [row[:mid] for row in M[:mid]]
    top_right = [row[mid:] for row in M[:mid]]
    bot_left = [row[:mid] for row in M[mid:]]
    bot_right = [row[mid:] for row in M[mid:]]
    return top_left, top_right, bot_left, bot_right

def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j]-B[i][j] for j in range(len(A))] for i in range(len(A))]

def combine(C11, C12, C21, C22):
    n = len(C11)
    C = [[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = C11[i][j]
            C[i][j+n] = C12[i][j]
            C[i+n][j] = C21[i][j]
            C[i+n][j+n] = C22[i][j]
    return C
```
