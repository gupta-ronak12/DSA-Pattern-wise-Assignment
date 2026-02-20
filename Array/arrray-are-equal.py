# Question 16:
# Check if two arrays are equal (both contain the same elements with the same frequencies).

def checkEqual(a, b):
    if len(a) != len(b):
        return False

    freq = {}

    for num in a:
        freq[num] = freq.get(num, 0) + 1

    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1

    return True


if __name__ == "__main__":
    a = [3, 5, 2, 5, 2]
    b = [2, 3, 5, 5, 2]

    print("true" if checkEqual(a, b) else "false")