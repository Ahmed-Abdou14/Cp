class Solution:
    
    def nthUglyNumber(self, n: int) -> int:
    
        uglies = [1]
        i2 = i3 = i5 = 0
    
        while len(uglies) < n:
            
            u2 = uglies[i2]*2
            u3 = uglies[i3]*3
            u5 = uglies[i5]*5
            
            if u2 == uglies[-1]:
                i2+=1
                u2 = uglies[i2]*2
            if u3 == uglies[-1]:
                i3+=1
                u3 = uglies[i3]*3
            if u5 == uglies[-1]:
                i5+=1
                u5 = uglies[i5]*5

            
            if u2 < u3 and u2 < u5:
                i2+=1
                uglies.append(u2)
            elif u3 < u5:
                i3 += 1
                uglies.append(u3)
            else:
                i5 += 1
                uglies.append(u5)
        
        return uglies[-1]

sol = Solution()
print(sol.nthUglyNumber(10))