# Question 33:
# Find the maximum difference (j - i) such that j > i and arr[i] <= arr[j].

def maxIndexDiff(arr):
    n = len(arr)
    if n == 0:
        return -1

    lMin = [0] * n
    rMax = [0] * n

    lMin[0] = arr[0]
    for i in range(1, n):
        lMin[i] = min(lMin[i - 1], arr[i])

    rMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rMax[i] = max(rMax[i + 1], arr[i])

    i = 0
    j = 0
    ans = -1

    while i < n and j < n:
        if lMin[i] <= rMax[j]:
            ans = max(ans, j - i)
            j += 1
        else:
            i += 1

    return ans


if __name__ == "__main__":
    arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    print(maxIndexDiff(arr))