from heapq import heappop, heappush, heapify

# # create empty heap
# H = []
# heapify(H)


# # Add elements
# heappush(H, -10)
# heappush(H, -3)
# heappush(H, -33)
# heappush(H, -40)

# # print max element
# print("Max : ", -H[0])

# # print heap max elements
# print("max elements:", [-i for i in H])

# # Pop max element
# heappop(H)

# # print after pop

# print("after pop max", [-i for i in H])

# # ---------------------------------------------------


def kthelement( arr, k):
    max_heap = []
    for val in arr:
        heappush(max_heap, -val)
        if len(max_heap) > k:
            heappop(max_heap)
    return -max_heap[0]

# S = Solution()
print(kthelement([1,32,11,9,5],3))


# Concept : 

# Python Max-Heap Logic (using heapq)The Problem: Python’s heapq module only implements a Min-Heap (the smallest value is always at index 0).
# The "-1 Trick": To simulate a Max-Heap, we multiply all numbers by -1 before pushing them.
# Logic: Inverting the signs flips the number line. The largest positive number becomes the smallest negative number, which the Min-Heap then pushes to the top.
# The Operations:Push: heappush(heap, -val) — Converts the value to negative to maintain "max" priority.
# Peek: -heap[0] — Multiplies by -1 again to view the original maximum value.
# Pop: -heappop(heap) — Removes the smallest negative and flips it back to the original positive maximum.
# Efficiency: This maintains $O(\log n)$ performance for insertions and deletions, which is much faster than calling max() on a list repeatedly ($O(n)$).


