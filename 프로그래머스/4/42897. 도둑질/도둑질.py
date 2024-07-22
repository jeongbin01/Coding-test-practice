def solution(money):
    n = len(money)
    
    if n == 1:
        return money[0]
    elif n == 2:
        return max(money)
    
    def rod(h):
        n = len(h)
        if n == 0:
            return 0
        elif n == 1:
            return h[0]
        elif n == 2:
            return max(h)
        
        dp = [0] * n
        dp[0] = h[0]
        dp[1] = max(h[0], h[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + h[i])
        
        return dp[-1]
    
    max_1 = rod(money[:-1])
    max_2 = rod(money[1:])
    
    return max(max_1, max_2)

print(solution([1, 2, 3, 1]))
print(solution([2, 3, 2]))  