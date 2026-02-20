# Question 11:
# Remove a given element from an array in-place and return the new length.

def removeElement(arr, val):
    idx = 0  

    for i in range(len(arr)):
        if arr[i] != val:
            arr[idx] = arr[i]
            idx += 1

    return idx


if __name__ == "__main__":
    arr = [3, 2, 2, 3]
    val = 3

    new_length = removeElement(arr, val)
    print("New length:", new_length)
    print("Array after removal:", arr[:new_length])