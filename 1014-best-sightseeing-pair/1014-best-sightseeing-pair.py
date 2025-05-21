class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, mx = 0, values[0]  # Initialize `ans` and `mx`
        for j in range(1, len(values)):  # Iterate through the array, starting from index 1
            ans = max(ans, values[j] - j + mx)  # Update the maximum score `ans`
            mx = max(mx, values[j] + j)  # Update the running maximum of `values[i] + i`
        return ans