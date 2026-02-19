# Question:
# Find the second largest element in an array using one traversal (one pass).

def getSecondLargest(arr):
    n = len(arr)
    
    if n < 2:
        return None  # Not enough elements

    largest = float('-inf')
    secondLargest = float('-inf')

    for num in arr:
        
        # Update largest and second largest
        if num > largest:
            secondLargest = largest
            largest = num
        
        # Update only second largest
        elif num > secondLargest and num != largest:
            secondLargest = num

    if secondLargest == float('-inf'):
        return None  # No second largest (all elements equal)

    return secondLargest


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))