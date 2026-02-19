# Question: # Find the minimum and maximum element in an array
# using optimal approach (comparing elements in pairs).

def findMinMax(arr):
    n = len(arr)

    # If array has only one element
    if n == 1:
        return arr[0], arr[0]

    # Initialize min and max
    if arr[0] < arr[1]:
        minimum = arr[0]
        maximum = arr[1]
    else:
        minimum = arr[1]
        maximum = arr[0]

    # Process elements in pairs
    for i in range(2, n, 2):
        
        # If last element is left alone (odd size array)
        if i == n - 1:
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i] > maximum:
                maximum = arr[i]
        else:
            # Compare elements in pair
            if arr[i] < arr[i + 1]:
                local_min = arr[i]
                local_max = arr[i + 1]
            else:
                local_min = arr[i + 1]
                local_max = arr[i]

            # Update global min and max
            if local_min < minimum:
                minimum = local_min
            if local_max > maximum:
                maximum = local_max

    return minimum, maximum


if __name__ == "__main__":
    arr = [3, 5, 1, 8, 2, 9]
    minimum, maximum = findMinMax(arr)
    print("Minimum:", minimum)
    print("Maximum:", maximum)