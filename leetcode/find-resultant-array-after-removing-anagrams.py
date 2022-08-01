class Solution(object):
    def removeAnagrams(self, words):
        if len(words) == 1: return words
        counters = list(map(lambda w: sorted(w), words))
        indexes = []
        i=j=0
        while j < len(counters):
            if counters[i] != counters[j]:
                indexes.append(i)
                i=j
            j+=1
        indexes.append(i if counters[-1] == counters[-2] else j-1)
        return list(map(lambda i: words[i], indexes))
                  
    
sol = Solution()
print(sol.removeAnagrams(["abba", "baba","bbaa","cd","cd"]))
print(sol.removeAnagrams(["a","b","c","d","e"]))