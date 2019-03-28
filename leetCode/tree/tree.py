# coding=utf-8
import re
import time

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 多叉树
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution():

    def __init__(self):
        self.t1 = TreeNode(3)
        self.t1.left  = TreeNode(0)
        self.t1.right = TreeNode(4)
        # self.t1.left.left = TreeNode(8)
        self.t1.left.right = TreeNode(2)
        self.t1.left.right.left = TreeNode(1)
        # self.t1.right.left = TreeNode(15)
        # self.t1.right.right = TreeNode(7)
        '''
            3
        9       20
      8   5    15  7   
        '''

        self.t2 = TreeNode(1)
        self.t2.left  = TreeNode(1)
        self.t2.right = TreeNode(3)
        self.t2.left.right = TreeNode(4)
        self.t2.right.right = TreeNode(7)

        self.node1 = Node(1, [3, 2, 4])
        self.node1.children[0] = Node(3, [5, 6])
        self.node1.children[0].children[0] = Node(5, [])
        self.node1.children[0].children[1] = Node(6, [])
        self.node1.children[1] = Node(2, [])
        self.node1.children[2] = Node(4, [])



        print("class leetCode tree init!")

    def __del__(self):
        print("class leetCode tree delete!")

    # 堆栈方式先序遍历
    def fronttack(self, root: TreeNode):
        print("先序遍历")
        # 空二叉树直接返回
        if not root:
            return
        outlist = []
        nood = root
        # 先续遍历
        while outlist or nood:
            # 循环遍历左分支
            while nood:
                print(nood.val)
                outlist.append(nood)
                nood = nood.left

            # 开始每层右分支遍历
            nood = outlist.pop()
            nood = nood.right

    # 二叉树迭代
    def mergeTrees(self, t1:TreeNode, t2:TreeNode) -> TreeNode:

        # print("func mergeTrees")
        # print("    Sloution1:")
        # print("        Runtime: 108 ms, faster than 33.36% of Python3 online submissions for Merge Two Binary Trees.")
        # print("        Memory Usage: 13.7 MB, less than 17.22% of Python3 online submissions for Merge Two Binary Trees.")
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        t1.val  += t2.val
        t1.left  = self.mergeTrees(t1.left,  t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return(t1)
        # 典型二叉树遍历

    def isUnivalTree(self, root: TreeNode) -> bool:
        print("func isUnivalTree")
        print("    Sloution1:")
        print("        Runtime: 52 ms, faster than 9.49% of Python3 online submissions for Univalued Binary Tree.")
        print("        Memory Usage: 13 MB, less than 5.36% of Python3 online submissions for Univalued Binary Tree.")

        def loopNode(node: TreeNode, value) -> bool:

            # node非空
            if node == None:
                return True
            if node.val != value:
                return False
            if loopNode(node.left, value) == False:
                return False
            if loopNode(node.right, value) == False:
                return False
            return True

        print(loopNode(root, root.val))
        return loopNode(root, root.val)

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        # print("func isUnivalTree")
        # print("    Sloution1:")
        # print("        Runtime: 92 ms, faster than 35.83% of Python3 online submissions for Search in a Binary Search Tree.")
        # print("        Memory Usage: 14.9 MB, less than 5.30% of Python3 online submissions for Search in a Binary Search Tree.")
        # nodeReturn = TreeNode(val)
        # def loopNode(node: TreeNode, value: int) -> bool:
        #     if node == None:
        #         return False
        #
        #     if node.val == value:
        #         nodeReturn.left = node.left
        #         nodeReturn.right = node.right
        #         return True
        #
        #     if loopNode(node.left, value) == True:
        #         return True
        #     if loopNode(node.right, value)== True:
        #         return True
        #     return False
        # if loopNode(root, val) == False:
        #     return []
        # print(nodeReturn)
        # return nodeReturn

        # print("    Sloution2:")
        # print("        Runtime: 84 ms, faster than 67.11% of Python3 online submissions for Search in a Binary Search Tree.")
        # print("        Memory Usage: 15.3 MB, less than 5.30% of Python3 online submissions for Search in a Binary Search Tree.")
        if root == None:
            return root

        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)
        else:

            return self.searchBST(root.right, val)

    # 层序遍历&取平均
    def averageOfLevels(self, root: TreeNode) -> list:
        print("func averageOfLevels")
        # print("    Sloution1:")
        # print("        Runtime: 64 ms")
        # print("        Memory Usage: 15.5 MB")
        templist  = []
        outlist   = []
        levelRead = 0
        sum = 0
        count = 0
        templist.append([root, 0])
        while templist:
            # 取出并删除节点
            node, level = templist.pop(0)

            # 同一级别
            if level == levelRead:
                sum += node.val
                count += 1
            # 进入新级别 对现有和取平均
            else:
                # print("sum = ",sum, "count = ", count, level, levelRead)
                outlist.append(sum / count)
                sum, count = node.val, 1
                levelRead = level

            # print(node.val,level)
            if node.left:
                templist.append([node.left, level + 1])

            if node.right:
                templist.append([node.right, level + 1])
        # 最后一层数据取平均
        outlist.append(sum / count)
        print(outlist)
        return outlist
        pass

    # 遍历求最大深度
    def maxDepth(self, root: TreeNode) -> int:
        # print("func maxDepth")
        # print("    Sloution1:")
        # print("        Runtime: 52 ms, faster than 54.12% of Python3 online submissions for Maximum Depth of Binary Tree.")
        # print("        Memory Usage: 14.4 MB, less than 82.75% of Python3 online submissions for Maximum Depth of Binary Tree.")
        if root:
            maxlevel = 1
            tempList = [[root, maxlevel]]
            # print(tempList)
            while tempList:
                node, level = tempList.pop(0)
                maxlevel = max(maxlevel, level)
                if node.left:
                    tempList.append([node.left,level + 1])
                if node.right:
                    tempList.append([node.right, level + 1])

            # print(maxlevel)
            return maxlevel
        else:
            return 0

    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        # print("func trimBST")
        # print("    Sloution1:")
        # print("        Runtime: 60 ms, faster than 73.22% of Python3 online submissions for Trim a Binary Search Tree.")
        # print("        Memory Usage: 17.3 MB, less than 5.36% of Python3 online submissions for Trim a Binary Search Tree.")
        def loopnode(node):
            if node:
                # 删除非L和R区间数据
                if node.val < L:
                    return loopnode(node.right)
                elif node.val > R:
                    return loopnode(node.left)
                else:
                    # 遍历二叉树
                    node.left  = loopnode(node.left)
                    node.right = loopnode(node.right)
                    return node
        # print(loopnode(root))
        return loopnode(root)

    # 多叉树层序遍历 用堆栈方式解决
    def levelOrder(self, root: Node) -> list:
        print("func levelOrder")
        print("    Sloution1:")
        print("        Runtime: 104 ms, faster than 47.03% of Python3 online submissions for N-ary Tree Level Order Traversal.")
        print("        Memory Usage: 17.8 MB, less than 5.47% of Python3 online submissions for N-ary Tree Level Order Traversal.")
        if root:
            outList = [[]]
            # print(outList)
            layer = 0
            maxLayer = 0
            tempList = [[root,layer]]

            # 使用堆栈层序遍历
            while tempList:
                node, layer = tempList.pop(0)
                # 每次进入新的一层新增list
                if layer > maxLayer:
                    maxLayer = layer
                    outList.append([node.val])
                else:
                    outList[layer].append(node.val)
                for data in node.children:
                    tempList.append([data, layer + 1])
        else:
            outList = []
        # print(outList)
        return outList

        # 多叉树遍历

    def postorder(self, root: Node) -> list:
        print("func postorder")
        # print("    Sloution1:")
        # print("        Runtime: 100 ms, faster than 46.61% of Python3 online submissions for N-ary Tree Postorder Traversal.")
        # print("        Memory Usage: 17.8 MB, less than 6.03% of Python3 online submissions for N-ary Tree Postorder ")
        outList = []
        if root == None:
            return outList

        def loopNode(nood: Node):
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

        def loopNode(nood: Node):

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

    def run(self):

        startTime = time.time()
        # self.mergeTrees(self.t1, self.t2)
        # self.isUnivalTree(self.t1)
        # print(self.searchBST(self.t1, 3))
        # self.averageOfLevels(self.t1)
        # self.maxDepth(self.t1)
        # self.trimBST(self.t1,1,3)
        # self.fronttack(self.t1)
        # self.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
        self.levelOrder(self.node1)

        endTime = time.time()

        print("class leetCode tree run time: ", (str(endTime - startTime))[:8], "s")

        pass

