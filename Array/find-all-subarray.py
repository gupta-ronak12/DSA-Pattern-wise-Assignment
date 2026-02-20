# Question 22:
# Find and print all non-empty subarrays of a given array.

def printSubarrays(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            subarr = []
            for k in range(i, j + 1):
                subarr.append(arr[k])
            print(*subarr)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    printSubarrays(arr)