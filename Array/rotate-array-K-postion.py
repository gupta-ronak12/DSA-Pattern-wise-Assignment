# Question 7:
# Rotate the array to the right by k positions (in-place).

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotateRight(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n  # Handle k > n

    # Step 1: Reverse entire array
    reverse(arr, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse(arr, 0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(arr, k, n - 1)

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    rotateRight(arr, k)
    print(*arr)