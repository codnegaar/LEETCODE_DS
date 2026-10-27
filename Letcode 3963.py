'''


'''

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [['#'] * n for _ in range(m)]
        r = c = 0
        
        res[r][c] = '.'
        
        while r < m - 1 or c < n - 1:
            if r < m - 1 and (c == n - 1 or abs((r + 1) * (n - 1) - c * (m - 1)) <= abs(r * (n - 1) - (c + 1) * (m - 1))):
                r += 1
            else:
                c += 1
                
            res[r][c] = '.'
            
        return [''.join(row) for row in res]
