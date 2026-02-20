# Question 29:
# Find the length of the longest consecutive sequence in an array.

def longestConsecutive(arr):
    st = set(arr)
    res = 0

    for val in arr:
        if val - 1 not in st:
            cur = val
            cnt = 0
            while cur in st:
                cur += 1
                cnt += 1
            res = max(res, cnt)

    return res


if __name__ == "__main__":
    arr = [2, 6, 1, 9, 4, 5, 3]
    print(longestConsecutive(arr))