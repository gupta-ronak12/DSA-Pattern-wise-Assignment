# Question 9:
# Remove duplicates from a sorted array while maintaining order.
# Modify the array in-place and return the new length.

def removeDuplicates(arr):
    n = len(arr)
    
    if n <= 1:
        return n

    idx = 1 

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr)

    print(*arr[:newSize])
