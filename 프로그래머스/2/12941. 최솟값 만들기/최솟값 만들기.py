def solution(A, B):
    
    A.sort()
    
    B.sort(reverse=True)
    
    t = 0
    for a, b in zip(A, B):
        t += a * b
        
    return t

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))  