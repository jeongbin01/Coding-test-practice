def solution(n, computers):
    def d(node):
        s = [node]
        while s:
            c = s.pop()
            for ne in range(n):
                if computers[c][ne] == 1 and not vi[ne]:
                    vi[ne] = True
                    s.append(ne)
    
    vi = [False] * n
    n_c = 0
    
    for i in range(n):
        if not vi[i]:
            vi[i] = True 
            d(i)
            n_c += 1
    
    return n_c
