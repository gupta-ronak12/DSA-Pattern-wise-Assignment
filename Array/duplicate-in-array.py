# Question 13:
# Find all duplicates in an array using the negative marking approach.


def findDuplicates(arr):
    duplicates = []

    for i in range(len(arr)):
        idx = abs(arr[i]) - 1  

    
        if arr[idx] < 0:
            duplicates.append(abs(arr[i]))
        else:
            
            arr[idx] = -arr[idx]

    return duplicates


if __name__ == "__main__":
    arr = [2, 3, 1, 2, 3]
    result = findDuplicates(arr)
    print(*result)