class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 0: return []
        def build(start, end):
            trees = []
            if start > end:
                return [None]
            for i in range(start, end+1):
                left = build(start, i-1)
                right = build(i+1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left, root.right = l, r
                        trees.append(root)
            return trees
        return build(1, n)
