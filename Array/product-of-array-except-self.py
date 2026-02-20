# Question 30:
# Product of Array Except Self:
# Given an array, return a new array where each element at index i
# is the product of all elements in the array except arr[i].
# Do not use division. 

def productExceptSelf(arr):
    n = len(arr)
    prefProduct = [1] * n
    suffProduct = [1] * n
    res = [0] * n

    for i in range(1, n):
        prefProduct[i] = arr[i - 1] * prefProduct[i - 1]

    for j in range(n - 2, -1, -1):
        suffProduct[j] = arr[j + 1] * suffProduct[j + 1]

    for i in range(n):
        res[i] = prefProduct[i] * suffProduct[i]

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    result = productExceptSelf(arr)
    print(*result)