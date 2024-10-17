import heapq
import math

def maxheap(arr):
    for i in range(len(arr)):
        arr[i] = -arr[i]
    heapq.heapify(arr)
    return arr

def operations(val):
    return math.ceil(val/3)

def max_value(arr, k):
    res = 0
    arr = maxheap(arr)
    for i in range(k):
        temp_val = -(heapq.heappop(arr))
        res += temp_val
        heapq.heappush(arr, -operations(temp_val))
    return res



arr = [1,10,3,3,3]
print(max_value(arr, 3))


    