import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    
    for _ in range(n):
        max_work = -heapq.heappop(works)
        if max_work > 0:
            heapq.heappush(works, -(max_work - 1))
        elif not works:
            break
    
    return sum(work ** 2 for work in works)

print(solution(4, [4, 3, 3]))  