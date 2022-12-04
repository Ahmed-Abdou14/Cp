class Solution:
    def __init__(self) -> None:
        self.v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
    def halvesAreAlike(self, s: str) -> bool:
        a, b =s[:len(s)//2], s[len(s)//2:]
        return not bool(self.countVowels(a) - self.countVowels(b))
    
    def countVowels(self, s: str) -> int:
        return sum([1 for c in s if c in self.v])

sol = Solution()
print(sol.halvesAreAlike("textbook"))
print(sol.halvesAreAlike("book"))