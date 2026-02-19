# Question:
# Find the sum of all elements in a given array (using iteration as it is better than recursion for this problem).

def sumArray(arr):
    total = 0
    
    for num in arr:
        total += num
    
    return total


if __name__ == "__main__":
    arr = [12, 3, 4, 15]
    print("Sum of given array is", sumArray(arr))