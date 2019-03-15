# couding=utf-8
import re
import time
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class SolutionEasy():

    def __init__(self):
        self.t1 = TreeNode(4)
        self.t1.left = TreeNode(2)
        self.t1.right = TreeNode(7)
        self.t1.left.left = TreeNode(1)
        self.t1.left.right = TreeNode(3)

        self.node1 = Node(1, [3,2,4])
        self.node1.children[0] = Node(3, [5,6])
        self.node1.children[0].children[0]= Node(5, [])
        self.node1.children[0].children[1] = Node(6, [])
        self.node1.children[1] = Node(2, [9])
        self.node1.children[1].children[0] = Node(9, [])
        self.node1.children[2] = Node(4, [])
        self.node2 = Node(44, [])
        print("class leetCode SolutionEasy init!")


    def __del__(self):
        print("class leetCode SolutionEasy delete!")

    # 多叉树遍历
    def postorder(self, root: Node) -> list:
        print("func postorder")
        # print("    Sloution1:")
        # print("        Runtime: 100 ms, faster than 46.61% of Python3 online submissions for N-ary Tree Postorder Traversal.")
        # print("        Memory Usage: 17.8 MB, less than 6.03% of Python3 online submissions for N-ary Tree Postorder ")
        outList = []
        if root == None:
            return outList

        def loopNode(nood:Node):
            # print("nood.children", nood.children)
            for data in nood.children:
                # print("data", data, "nood.val", nood.val)
                loopNode(data)
            outList.append(nood.val)
            # print("outList", outList)

        loopNode(root)
        # print(outList)
        return outList

    # 多叉树遍历逆序
    def preorder(self, root: Node) -> list:
        print("func preorder")
        # print("    Sloution1:")
        # print("        Runtime: 104 ms, faster than 25.06% of Python3 online submissions for N-ary Tree Preorder Traversal.")
        # print("        Memory Usage: 17.8 MB, less than 5.26% of Python3 online submissions for N-ary Tree Preorder Traversal. ")
        outList = []
        def loopNode(nood:Node):

            if nood:
                outList.append(nood.val)
                # print("nood.children", nood.children)
                for data in nood.children:
                    # print("data", data, "nood.val", nood.val)
                    loopNode(data)

            # print("outList", outList)

        loopNode(root)
        print(outList)
        return outList

    # 多维数组取极值与非零值
    def projectionArea(self, grid) -> int:
        print("func projectionArea")
        # print("    Sloution1:")
        # print("        Runtime: 44 ms, faster than 73.14% of Python3 online submissions for Projection Area of 3D Shapes.")
        # print("        Memory Usage: 13.3 MB, less than 7.84% of Python3 online submissions for Projection Area of 3D Shapes. ")
        sum = 0

        # 遍历 累加最大值和非零值个数
        for listSub in grid:
            sum += max(listSub)
            for data in listSub:
                if data != 0:
                    sum += 1

        # 横纵坐标变换 累加最大值
        for listSub in zip(*grid):
            sum += max(listSub)
        print(sum)
        return sum

    # 遍历多叉树最大深度
    def maxDepth(self, root: Node) -> int:
        print("func maxDepth")
        # print("    Sloution1:")
        # print("        Runtime: 104 ms, faster than 14.93% of Python3 online submissions for Maximum Depth of N-ary Tree.")
        # print("        Memory Usage: 17.6 MB, less than 5.30% of Python3 online submissions for Maximum Depth of N-ary Tree.")
        Maxdeep = 0

        if not root:
            return 0
        def loop(node:Node, realdeep:int):
            nonlocal Maxdeep
            # 每一次loop进入更深以及
            realdeep += 1
            Maxdeep = max(realdeep, Maxdeep)
            # for循环内是同级deep
            for sub in node.children:
                # 循环遍历每个分支
                loop(sub, realdeep)

            # 退出当前层级
            return
            # return deep
        loop(root, Maxdeep)
        print("Maxdeep =", Maxdeep)
        return Maxdeep


    def run(self):

        startTime = time.time()

        # self.postorder(self.node1)
        # self.preorder(self.node1)
        # self.projectionArea([[2,2,2],[2,1,3],[2,2,2]])
        self.maxDepth(self.node1)
        endTime = time.time()
        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

