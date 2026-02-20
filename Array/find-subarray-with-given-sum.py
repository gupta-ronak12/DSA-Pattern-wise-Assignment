# Question 19:
# Find a subarray with a given sum (return 1-based start and end indices).

def subarraySum(arr, target):
    s = 0
    curr = 0

    for e in range(len(arr)):
        curr += arr[e]

        while curr > target and s < e:
            curr -= arr[s]
            s += 1

        if curr == target:
            return [s + 1, e + 1]

    return [-1]


if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
    result = subarraySum(arr, target)
    print(*result)