# Question 24:
# Rearrange positive and negative numbers in an array alternately.

def rearrange(arr):
    pos = []
    neg = []

    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    posIdx = 0
    negIdx = 0
    i = 0

    while posIdx < len(pos) and negIdx < len(neg):
        if i % 2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        i += 1

    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1

    while negIdx < len(neg):
        arr[i] = neg[negIdx]
        negIdx += 1
        i += 1


if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]
    rearrange(arr)
    print(*arr)