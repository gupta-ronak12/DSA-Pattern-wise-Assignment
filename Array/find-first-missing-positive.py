# Question 27:
# Find the first missing positive integer in an array.

def missingNumber(arr):
    n = len(arr)

    for i in range(n):
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            correct_idx = arr[i] - 1
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    arr = [2, -3, 4, 1, 1, 7]
    print(missingNumber(arr))