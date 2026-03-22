#Date: 2025-06-21
# find the largest element in a array
arr= [1, 2, 3, 4, 5]
largest = max(arr)
print("Largest element in the array is:", largest)

# find the smallest element in a array
smallest = min(arr)
print("Smallest element in the array is:", smallest)

# Reeverse an array
arr.sort(reverse=True)
print("Reversed array is:", arr)

# check if an array is sorted
if arr == sorted(arr):
    print("Array is sorted")    
else:
    print("Array is not sorted")

# remove duplicates from an array
arr1 = [1, 2, 2, 3, 4, 4, 5]
arr1 = list(set(arr))
print("Array after removing duplicates is:", arr1)

# Rotate an array by k elements
arr2 = [1, 2, 3, 4, 5]
k = 2
arr2 = arr2[k:] + arr2[:k]
print("Array after rotating by", k, "elements is:", arr2)

# Find the intersection of two arrays
arr3 = [1, 2, 3, 4, 5]
arr4 = [4, 5, 6, 7, 8]
intersection = list(set(arr3) & set(arr4))
print("Intersection of the two arrays is:", intersection)

# Find the union of two arrays
arr5 = [1, 2, 3, 4, 5]
arr6 = [4, 5, 6, 7, 8]
union = list(set(arr5) | set(arr6))
print("Union of the two arrays is:", union) 

# Find the SECOND LARGEST element in an array
arr7 = [1, 2, 3, 4, 5]
arr7.sort(reverse=True)
print(arr7[1], "is the second largest element in the array")

# MERGE two sorted arrays
arr8 = [1, 3, 5]
arr9 = [2, 4, 6]
merged_array = sorted(arr8 + arr9)
print("Merged sorted array is:", merged_array)

# Find the Kth largest element in an array
arr10 = [3, 1, 4, 1, 5, 9, 2, 6, 5]     
k = 3
arr10.sort(reverse=True)
kth_largest = arr10[k-1] if k <= len(arr10) else None
print(f"The {k}th largest element in the array is:", kth_largest)



