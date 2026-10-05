class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS,COLS = len(heights),len(heights[0])
        pacific_reach  = set()
        atlantic_reach = set()

        def dfs(r,c,visited,prev_height):
            if ((r,c) in visited or r<0 or c<0 or r>=ROWS or c>=COLS or heights[r][c] < prev_height):
                return
            visited.add((r,c))
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(dr+r,dc+c,visited,heights[r][c])
        for c in range(COLS):
            dfs(0,c,pacific_reach,heights[0][c])
            dfs(ROWS-1,c,atlantic_reach,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0,pacific_reach,heights[r][0])
            dfs(r,COLS-1,atlantic_reach,heights[r][COLS-1])
        return list(map(list,pacific_reach.intersection(atlantic_reach)))
        