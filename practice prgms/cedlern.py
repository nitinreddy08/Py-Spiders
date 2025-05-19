# def binarySearch(arr, targetVal):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == targetVal:
#             return mid
        
#         if arr[mid] < targetVal:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# myTarget = 15

# result = binarySearch(myArray, myTarget)

# if result != -1:
#     print("Value",myTarget,"found at index", result)
# else:
#     print("Target not found in array.")






# def merge_sort():
#     # Base case: if the array is of length 1 or empty, it's already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Find the middle index and divide the array into two halves
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
    
#     # Recursively sort both halves
#     left_sorted = merge_sort(left_half)
#     right_sorted = merge_sort(right_half)
    
#     # Merge the two sorted halves
#     return merge(left_sorted, right_sorted)

# def merge(left, right):
#     result = []
#     i = j = 0
    
#     # Merge the two arrays by comparing their elements one by one
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     # If any elements remain in either left or right array, append them to the result
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result

# # Example usage
# arr = [3, 6, 8, 10, 1, 2, 1]
# sorted_arr = merge_sort(arr)
# print(sorted_arr)







def Qs(arr):
    if len(arr) <= 1:
        return arr  # Base case: array of length 1 is already sorted
    pivot = arr[len(arr) // 2]  # Select middle element as pivot
    left, middle, right = [], [], []  # Initialize three lists for partitioning
    
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)
    
    return Qs(left) + middle + Qs(right)  # Recursively sort and merge

arr1=[3, 6, 8, 10, 1, 2, 1]
arr2= [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
res = arr1+arr2
sorted_arr = Qs(res)
print ((list(set(sorted_arr)))[8])

