# Solution 20: Sort a Linked List using Merge Sort

## Approach Explanation
Find the middle of the list using slow/fast pointers. Split into two halves. Recursively sort each half, then merge the two sorted halves.

## Step-by-Step Logic
1. Base case: empty list or single node.
2. Find middle using slow/fast pointers. Split at middle.
3. Recursively sort both halves.
4. Merge two sorted lists.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(log N) for recursion stack.

## Code
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_list(head):
    if not head or not head.next:
        return head
    
    # Find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None
    
    left = sort_list(head)
    right = sort_list(mid)
    
    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 or l2
    return dummy.next
```
