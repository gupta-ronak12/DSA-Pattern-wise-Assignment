# Question 20:
# Rotate the array to the left by k positions (in-place)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotateLeft(arr, k):
    n = len(arr)
    if n == 0:
        return

    k = k % n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    rotateLeft(arr, k)
    print(*arr)