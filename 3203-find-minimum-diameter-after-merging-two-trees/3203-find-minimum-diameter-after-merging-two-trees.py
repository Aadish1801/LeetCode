from typing import List
from collections import defaultdict

class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        # Calculate the diameter of each tree
        diameter1 = self.treeDiameter(edges1)
        diameter2 = self.treeDiameter(edges2)
      
        # The minimum diameter after merging is the maximum of the two diameters
        # or the sum of half of each diameter plus one.
        return max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        # Depth-first search to find the farthest node from the starting node.
        def dfs(node: int, parent: int, depth: int):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1)
          
            nonlocal max_depth, farthest_node
            if max_depth < depth:
                max_depth = depth
                farthest_node = node

        # Build the adjacency list representation of the graph.
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # Initialize variables for the maximum depth and farthest node.
        max_depth = farthest_node = 0
        # First DFS to find one endpoint of the diameter
        dfs(0, -1, 0)
        # Second DFS from the farthest node found to determine the diameter
        dfs(farthest_node, -1, 0)
      
        return max_depth