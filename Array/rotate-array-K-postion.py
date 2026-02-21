# Question 7:
# Rotate the array to the right by k positions (in place).

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotateRight(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n 

    reverse(arr, 0, n - 1)

    reverse(arr, 0, k - 1)

    reverse(arr, k, n - 1)

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    rotateRight(arr, k)
    print(*arr)
