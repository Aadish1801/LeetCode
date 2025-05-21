class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:  # If the [tree](/problems/tree_intro) is empty, there are no values to process, return an empty list.
            return []
        q = deque([root])  # Initialize the deque with the root node to start the level order traversal.
        ans = []  # This list will store the largest values for each level.
      
        # Continue the loop as long as there are nodes to process.
        while q:  
            t = -inf  # Set the maximum value for current level to negative infinity.
          
            # Process each node of the current level.
            for _ in range(len(q)):  # 'for' loop runs for the number of nodes in the current level.
                node = q.popleft()  # Dequeue the front node of the queue.
                t = max(t, node.val)  # Update the maximum value if node's value is greater.
              
                # Enqueue children of the current node if they exist.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
          
            # After processing the current level, the largest value is appended to the answer.
            ans.append(t)
      
        # Return the array containing the largest values for each level.
        return ans