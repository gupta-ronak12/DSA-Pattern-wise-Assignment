# Question:
# Count frequency of each element in an array.

def countFrequency(arr):
    freq_map = {}

    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    return freq_map


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 1, 4, 2]
    print(countFrequency(arr))