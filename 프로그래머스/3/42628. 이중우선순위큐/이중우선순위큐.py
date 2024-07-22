def solution(operations):
    q = []
    
    for operation in operations:
        if operation[0] == 'I':
            num = int(operation[2:])
            q.append(num)
        elif operation == 'D 1' and q:
            q.remove(max(q))
        elif operation == 'D -1' and q:
            q.remove(min(q))
        
    if not q:
        return [0, 0]
    else:
        return [max(q), min(q)]

print(solution(["I 16", "D 1"])) 
print(solution(["I 7", "I 5", "I -5", "D -1"]))  
