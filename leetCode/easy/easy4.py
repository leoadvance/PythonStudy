# couding=utf-8
import re
import time
import collections
import operator

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class SolutionEasy():

    def __init__(self):
        self.t1 = TreeNode(3)
        self.t1.left = TreeNode(5)
        self.t1.right = TreeNode(1)
        self.t1.left.left = TreeNode(6)
        self.t1.left.right = TreeNode(2)
        self.t1.left.right.left = TreeNode(7)
        self.t1.left.right.right = TreeNode(4)
        self.t1.right.right = TreeNode(1)
        self.t1.right.right.left = TreeNode(9)
        self.t1.right.right.right = TreeNode(8)

        self.t2 = TreeNode(3)
        self.t2.left = TreeNode(5)
        self.t2.right = TreeNode(1)
        self.t2.left.left = TreeNode(6)
        self.t2.left.right = TreeNode(2)
        self.t2.left.right.left = TreeNode(7)
        self.t2.left.right.right = TreeNode(4)
        self.t2.right.right = TreeNode(1)
        self.t2.right.right.left = TreeNode(9)
        self.t2.right.right.right = TreeNode(8)

        self.node1 = Node(1, [3,2,4])
        self.node1.children[0] = Node(3, [5,6])
        self.node1.children[0].children[0]= Node(5, [])
        self.node1.children[0].children[1] = Node(6, [])
        self.node1.children[1] = Node(2, [9])
        self.node1.children[1].children[0] = Node(9, [])
        self.node1.children[2] = Node(4, [])
        self.node2 = Node(44, [])

        self.listNode = ListNode(1)
        self.listNode.next = ListNode(2)
        self.listNode.next.next = ListNode(3)
        self.listNode.next.next.next = ListNode(4)
        self.listNode.next.next.next.next = ListNode(5)
        print("class leetCode SolutionEasy init!")


    def __del__(self):
        print("class leetCode SolutionEasy delete!")


    # 数据求余
    def numberOfLines(self, widths: list, S: str) -> list:
        print("func numberOfLines")
        # print("    Sloution1:")
        # print("        Runtime: 36 ms, faster than 73.24% of Python3 online submissions for Number of Lines To Write String.")
        # print("        Memory Usage: 13.1 MB, less than 7.14% of Python3 online submissions for Number of Lines To Write String.")
        # listOut = [0,0]
        # if S:
        #     listOut[0] = 1
        # for char in S:
        #     listOut[1] += widths[ord(char) - 97]
        #     if listOut[1] > 100:
        #         listOut[1] = widths[ord(char) - 97]
        #         listOut[0] += 1
        # print(listOut)
        # return listOut

        # print("    Sloution2:")
        # print("        Runtime: 48 ms, faster than 23.86% of Python3 online submissions for Number of Lines To Write String.")
        # print("        Memory Usage: 13.2 MB, less than 7.14% of Python3 online submissions for Number of Lines To Write String.")
        line = 1
        count = 0
        for char in S:
            count += widths[ord(char) - 97]
            if count > 100:
                count = widths[ord(char) - 97]
                line += 1
        print([line, count])
        return [line, count]

    # 二叉树比较
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        print("func leafSimilar")
        # print("    Sloution1:")
        # print("        Runtime: 40 ms, faster than 56.81% of Python3 online submissions for Leaf-Similar Trees.")
        # print("        Memory Usage: 13.2 MB, less than 5.32% of Python3 online submissions for Leaf-Similar Trees.")
        outlist1 = []
        outlist2 = []

        # 迭代提取出要比较的list
        def loopNode(node:TreeNode, outlist):
            if node:
                if node.left == None and node.right == None :
                    outlist.append(node.val)
                    return
                loopNode(node.left,  outlist)
                loopNode(node.right, outlist)
        loopNode(root1, outlist1)
        loopNode(root2, outlist2)
        print(operator.eq(outlist1, outlist2))
        return operator.eq(outlist1, outlist2)

    # 二进制取反
    def findComplement(self, num: int) -> int:
        print("func findComplement")
        # print("    Sloution1:")
        # print("        Runtime: 48 ms, faster than 24.92% of Python3 online submissions for Number Complement.")
        # print("        Memory Usage: 13.2 MB, less than 5.55% of Python3 online submissions for Number Complement.")
        # 通过异或取反，并过滤"0b"
        # temp = bin(num ^ 0xFFFFFFFF)[2:]
        #
        # # 找到字符串中"0"以后的字段，再通过int转换成10进制
        # print(int(temp[temp.index("0"):], 2))
        # return(int(temp[temp.index("0"):], 2))

        # print("    Sloution2:")
        # print("        Runtime: 36 ms, faster than 85.67% of Python3 online submissions for Number Complement.")
        # print("        Memory Usage: 13.1 MB, less than 5.55% of Python3 online submissions for Number Complement.")

        # 10进制转str二进制
        temp = bin(num)[2:]
        out = ""

        # 遍历取反
        for s in temp:
            if s == "0":
                out += "1"
            else:
                out += "0"
        # print(int(out,2))
        return(int(out,2))

    def findWords(self, words: list) -> list:
        print("func findWords")
        # print("    Sloution1:")
        # print("        Runtime: 36 ms, faster than 61.81% of Python3 online submissions for Keyboard Row.")
        # print("        Memory Usage: 13.2 MB, less than 6.58% of Python3 online submissions for Keyboard Row.")
        tupleTemp = ("qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM")
        outList = []
        for strdata in words:
            sign = True
            # 获取首字符在tuple中位置
            for i in range(len(tupleTemp)):
                if strdata[0] in tupleTemp[i]:
                    break
            for char in strdata[1:]:
                # 发现不在同一行字符 退出循环
                if char not in tupleTemp[i]:
                    sign = False
                    break
            if sign:
                outList.append(strdata)
        print(outList)
        return outList

    def run(self):

        startTime = time.time()

        # self.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")
        # self.leafSimilar(self.t1, self.t2)
        # self.findComplement(5)
        self.findWords(["Hello", "Alaska", "Dad", "Peace"])
        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

