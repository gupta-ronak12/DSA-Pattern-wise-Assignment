# Question 17:
# Find the leader elements in an array.
# An element is a leader if it is greater than all elements to its right.

def findLeaders(arr):
    n = len(arr)
    leaders = []

    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
            
    leaders.reverse()
    return leaders


if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = findLeaders(arr)
    print(*result)
