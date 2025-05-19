def Qs(arr):
    if len(arr) <= 1:
        return arr
    middle = arr[len(arr) // 2],
    left, middle, right = [], [], []
    
    for element in arr:
        if element < middle:
            left.append(element)
        elif element == middle:
            middle.append(element)
        else:
            right.append(element)
    
    return Qs(left) + middle + Qs(right)

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = Qs(arr)
print(sorted_arr)