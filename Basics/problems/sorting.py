#1- Bubble Sort\
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for i in range(0, n-i-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
                if not swapped:
                    break
arr=[5,3,8,4,2]
bubble_sort(arr)
print("Sorted array: ", arr)        

#2 - implement selection sort

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index],arr[i]
arr=[5,3,8,4,2]
selection_sort(arr)
print("Sorted array: ", arr)

#3 - implement insertion sort
def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr=[5,3,8,4,2]
insertion_sort(arr)
print("Sorted array: ", arr)

#4 - implement merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
arr = [5, 3, 8, 4, 2]
merge_sort(arr)
print("Sorted array: ", arr)

# 5 - implement quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr = [5, 3, 8, 4, 2]
sorted_arr = quick_sort(arr)
print("Sorted array: ", sorted_arr)

#6 - implement bubble search
def bubble_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1
arr = [5, 3, 8, 4, 2]
target = 4
result = bubble_search(arr, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

#7 - find the first and last occurrence of an element in a sorted array
def find_first_and_last(arr, target):
    first = last = -1
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return (first, last)
arr = [2, 3, 4, 4, 4, 5, 8]
target = 4
first, last = find_first_and_last(arr, target)
print("First occurrence:", first)
print("Last occurrence:", last)

#8 - find the kth smallest element in an unsorted array
def kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None
    arr.sort()
    return arr[k-1]
arr = [5, 3, 8, 4, 2]
k = 3   
result = kth_smallest(arr, k)
print("The", k, "th smallest element is:", result)

#9 - sort an array of 0s, 1s, and 2s(Dutch National Flag Problem)
def dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
arr = [0, 1, 2, 0, 1, 2, 0]
sorted_arr = dutch_national_flag(arr)
print("Sorted array: ", sorted_arr)

#10 - find the missing number in a sorted array
def find_missing_number(arr):   
    n = len(arr)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
arr = [1, 2, 4, 5, 6]
missing_number = find_missing_number(arr)
print("Missing number is:", missing_number)
