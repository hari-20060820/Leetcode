class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def solve(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = solve(left, mid - 1)
            node.right = solve(mid + 1, right)

            return node

        return solve(0, len(nums) - 1)