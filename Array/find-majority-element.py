# Question 25:
# Find the majority element in an array (element that appears more than n/2 times).

def majorityElement(arr):
    n = len(arr)
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > n // 2:
        return candidate
    return -1


if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    print(majorityElement(arr))