# Question 32:
# Find Maximum Product Pair: Find two elements in the array whose product is maximum.

def maxProduct(arr):
    n = len(arr)

    if n < 2:
        print("No pairs exist")
        return

    if n == 2:
        print("Max product pair is {", arr[0], ",", arr[1], "}")
        return

    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if max1 * max2 >= min1 * min2:
        print("Max product pair is {", max1, ",", max2, "}")
    else:
        print("Max product pair is {", min1, ",", min2, "}")


if __name__ == "__main__":
    arr = [1, 4, 3, 6, 7, 0]
    maxProduct(arr)