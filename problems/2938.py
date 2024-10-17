def minimumSteps(s):
        n = len(s)
        cnt = 0
        ans = 0
        
        for i in range(n):
            if s[i] == '0':
                ans += i - cnt
                cnt += 1
        
        return ans
        
            
            
print(minimumSteps("11000111"))
