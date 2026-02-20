# Question 28:
# Sort an array of 0s, 1s, and 2s using the Dutch National Flag algorithm.

def sort012(arr):
    n = len(arr)
    lo = 0
    mid = 0
    hi = n - 1

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1


if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    sort012(arr)
    print(*arr)