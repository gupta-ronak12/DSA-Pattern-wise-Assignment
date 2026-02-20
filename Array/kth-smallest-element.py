# Question 21:
# Find the Kth smallest element in an array.

import heapq

def kthSmallest(arr, k):
    max_heap = []

    for num in arr:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return -max_heap[0]


if __name__ == "__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k = 4
    print(kthSmallest(arr, k))