def solution(s):
    t = []
    
    for char in s:
        if char == '(':
            t.append(char)
        elif char == ')':
            if not t:
                return False
            t.pop()
    
    return len(t) == 0
            