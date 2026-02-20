# Question 14:
# Find the intersection of two arrays (return unique common elements between two arrays).

def intersect(a, b):
    
    setA = set(a)
    result = []

    for elem in b:
        if elem in setA:
            result.append(elem)
            setA.remove(elem) 

    return result


if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 6, 3, 4]

    output = intersect(a, b)
    print(*output)