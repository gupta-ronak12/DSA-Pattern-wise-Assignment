# Question 6:
# Check if an array is sorted in non Decreasing order

def isSorted(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            return False

    return True


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]

    if isSorted(arr):
        print("true")
    else:
        print("false")
