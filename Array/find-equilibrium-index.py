# Question 31:
# Find the equilibrium index in an array such that
# the sum of elements on the left equals the sum on the right.

def equilibriumPoint(arr):
    total = sum(arr)
    prefSum = 0

    for pivot in range(len(arr)):
        suffSum = total - prefSum - arr[pivot]
        if prefSum == suffSum:
            return pivot
        prefSum += arr[pivot]

    return -1


if __name__ == "__main__":
    arr = [1, 7, 3, 6, 5, 6]
    print(equilibriumPoint(arr))