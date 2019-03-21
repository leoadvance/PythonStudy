# couding=utf-8
import re
import time

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():

    def __init__(self):
        self.t1 = TreeNode(3)
        self.t1.left  = TreeNode(9)
        self.t1.right = TreeNode(20)
        self.t1.right.left = TreeNode(15)
        self.t1.right.right = TreeNode(7)


        self.t2 = TreeNode(1)
        self.t2.left  = TreeNode(1)
        self.t2.right = TreeNode(3)
        self.t2.left.right = TreeNode(4)
        self.t2.right.right = TreeNode(7)
        #

        print("class leetCode tree init!")

    def __del__(self):
        print("class leetCode tree delete!")

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

    def run(self):

        startTime = time.time()
        # self.mergeTrees(self.t1, self.t2)
        # self.isUnivalTree(self.t1)
        # print(self.searchBST(self.t1, 3))
        self.averageOfLevels(self.t1)
        endTime = time.time()
        print("class leetCode tree run time: ", (str(endTime - startTime))[:8], "s")

        pass

