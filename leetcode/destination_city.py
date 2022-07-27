class Solution:
    def destCity(self, paths) -> str:
        sources = set(map(lambda r: r[0], paths))
        cities = set([city for routes in paths for city in routes])
        return list(cities.difference(sources))[0]
    
sol = Solution()
print(sol.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))