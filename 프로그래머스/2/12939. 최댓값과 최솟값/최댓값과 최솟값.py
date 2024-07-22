def solution(s):
    m = list(map(int, s.split()))
    
    n = min(m)
    x = max(m)
    
    return f"{n} {x}"

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))