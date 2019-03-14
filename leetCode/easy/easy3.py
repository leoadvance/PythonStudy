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
        self.node1.children[1] = Node(2, [])
        self.node1.children[2] = Node(4, [])
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

        pass

    def run(self):

        startTime = time.time()

        # self.postorder(self.node1)
        # self.preorder(self.node1)
        self.projectionArea([[2,2,2],[2,1,3],[2,2,2]])
        endTime = time.time()
        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

