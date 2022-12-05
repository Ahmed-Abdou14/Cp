from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        l, r, t, b, lt, lb, rt, rb = None, None, None, None, None, None, None, None
        ki, kj = king
        
        for qi, qj in queens:
            
            if abs(qi - ki) == abs(qj - kj):
                # CHECK DIAGONALS
                if qi < ki and qj < kj:
                    # LEFT TOP
                    if lt is None:
                        lt = [qi, qj]
                    else:
                        if qi > lt[0]:
                            lt = [qi, qj]
                elif qi < ki and qj > kj:
                    # RIGHT TOP
                    if rt is None:
                        rt = [qi, qj]
                    else:
                        if qi > rt[0]:
                            rt = [qi, qj]
                elif qi > ki and qj < kj:
                    # LEFT BOTTOM
                    if lb is None:
                        lb = [qi, qj]
                    else:
                        if qi < lb[0]:
                            lb = [qi, qj]
                elif qi > ki and qj > kj:
                    # RIGHT BOTTOM
                    if rb is None:
                        rb = [qi, qj]
                    else:
                        if qi < rb[0]:
                            rb = [qi, qj]
            elif qi == ki:
                # CHECK HORIZONTAL
                if qj < kj:
                    # LEFT
                    if l is None:
                        l = [qi, qj]
                    else:
                        if qj > l[1]:
                            l = [qi, qj]
                elif qj > kj:
                    # RIGHT
                    if r is None:
                        r = [qi, qj]
                    else:
                        if qj < r[1]:
                            r = [qi, qj]
            elif qj == kj:
                # CHECK VERTICAL
                if qi < ki:
                    # TOP
                    if t is None:
                        t = [qi, qj]
                    else:
                        if qi > t[0]:
                            t = [qi, qj]
                elif qi > ki:
                    # BOTTOM
                    if b is None:
                        b = [qi, qj]
                    else:
                        if qi < b[0]:
                            b = [qi, qj]
                        
        return list(filter(lambda x: x, [l, r, t, b, lt, lb, rt, rb]))

sol = Solution()
print(sol.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]))
print(sol.queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3]))
print(sol.queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4]))