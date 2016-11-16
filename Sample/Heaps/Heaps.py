import heapq
import collections
def kth_magic(k):
    if k < 1: return False
    next_value = 1
    prev_value = 0
    # Find the kth magic number
    a = [1]
    heapq.heapify(a)
    count = 0
    while(count < k):
        next_value = heapq.heappop(a)
        if prev_value == next_value: continue
        heapq.heappush(a, next_value * 3)
        heapq.heappush(a, next_value * 5)
        heapq.heappush(a, next_value * 7)
        prev_value = next_value
        count += 1
    return next_value

def kath_magic_nospace(k):
    if k < 1: return False
    next_value = 1
    a3 = collections.deque([3])
    a5 = collections.deque([5])
    a7 = collections.deque([7])
    k = k-1
    count = 0
    while count < k:
        next_value = min([a3[0],a5[0],a7[0]])
        if next_value == a3[0]: a3.popleft()
        if next_value == a5[0]: a5.popleft()
        if next_value == a7[0]: a7.popleft()
        a3.append(next_value*3)
        a5.append(next_value*5)
        a7.append(next_value*7)
        count += 1
    return next_value
