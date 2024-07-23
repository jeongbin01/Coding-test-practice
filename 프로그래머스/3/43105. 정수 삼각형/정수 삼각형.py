def solution(triangle):
    
    a = triangle[-1]
    
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            
            a[j] = triangle[i][j] + max(a[j], a[j+1])
            
    return a[0]