# Question 18:
# Move all zeroes in an array to the end while maintaining the order of non-zero elements.

def pushZerosToEnd(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    print(*arr)