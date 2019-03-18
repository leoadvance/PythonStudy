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
        self.t1 = TreeNode(5)
        self.t1.left = TreeNode(3)
        self.t1.right = TreeNode(6)
        self.t1.left.left = TreeNode(2)
        self.t1.left.right = TreeNode(4)
        self.t1.left.left.left = TreeNode(1)
        self.t1.right.right = TreeNode(8)
        self.t1.right.right.left = TreeNode(7)
        self.t1.right.right.right = TreeNode(9)

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


    def run(self):

        startTime = time.time()

        self.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")
        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

