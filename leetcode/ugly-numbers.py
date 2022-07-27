class Solution:
    def isUgly(self, n: int) -> bool:
        #check for every number from 1 to N
        for i in range(1, n+1):
            if(self.isPrime(i)):
                if i not in [2,3,5]:
                    return False
        return True
        
    def isPrime(self, n):
        if(n == 1 or n == 0):return False
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True


# Driver code
N = 100

    
sol = Solution()
print(sol.isUgly(6))
print(sol.isUgly(1))
print(sol.isUgly(14))