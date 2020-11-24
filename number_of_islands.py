'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        for i, raw in enumerate(grid):
            for j, col in enumerate(raw):

                if(grid[i][j] == '1'):
                    islands += 1
                    self.flood_bfs(i,j, grid)

        return islands

    def flood_bfs(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return
        else:
            grid[i][j] = '0'
            self.flood_bfs( i+1, j, grid)
            self.flood_bfs( i-1, j, grid)
            self.flood_bfs( i, j+1, grid)
            self.flood_bfs( i, j-1, grid)
