# Question 12:
# Find the missing number in an array of size n containing numbers from 1 to n.

def missingNum(arr):
    n = len(arr) + 1  
    
    total_sum = sum(arr)
    
    expected_sum = n * (n + 1) // 2
    
    return expected_sum - total_sum


if __name__ == "__main__":
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))
