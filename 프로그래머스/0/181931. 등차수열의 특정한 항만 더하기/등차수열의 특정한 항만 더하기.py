def solution(a, d, included):
    t = 0  
    
    for i in range(len(included)):
        term = a + i * d 
        if included[i]:  
            t += term  
    
    return t