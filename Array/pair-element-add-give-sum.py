# Question 8:
# Find a pair of elements in the array that adds up to a given target sum.

def twoSum(arr, target):
    seen = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            return (complement, num)

        seen.add(num)

    return None


if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    result = twoSum(arr, target)

    if result:
        print("Pair found:", result)
    else:
        print("No pair found")