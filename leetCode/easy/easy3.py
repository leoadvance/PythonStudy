# coding=utf-8
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
            # nonlocal 表明使用外层变量
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

    # 求list最大最小差值
    def smallestRangeI(self, A: list, K: int) -> int:
        print("func smallestRangeI")
        # print("    Sloution1:")
        # print("        Runtime: 56 ms, faster than 36.08% of Python3 online submissions for Smallest Range I.")
        # print("        Memory Usage: 14.1 MB, less than 8.33% of Python3 online submissions for Smallest Range I.")
        if len(A) == 1:
            return 0

        # 数组升序排序
        A.sort(reverse = False)

        smallest = A[-1] - A[0] - 2*K

        if (smallest < 0):
            return 0
        else:
            return smallest


        pass

    # 字符串分割统计
    def subdomainVisits(self, cpdomains: list) -> list:
        print("func subdomainVisits")
        # print("    Sloution1:")
        # print("        Runtime: 64 ms, faster than 53.80% of Python3 online submissions for Subdomain Visit Count.")
        # print("        Memory Usage: 13.4 MB, less than 7.07% of Python3 online submissions for Subdomain Visit Count.")
        # 声明dict
        dictTemp = {}

        # 遍历 分割
        for string in cpdomains:
            # 分割字符串
            num, value = string.split(" ")
            num = int(num)
            listTemp   = value.split(".")
            # print("listTemp", listTemp,num)
            strLen = len(listTemp)
            # 如果有三个子域名 新增key
            if strLen > 2:
                dictTemp[value] = num
            # 增加lowlevel
            if strLen > 1:
                lowLevel = listTemp[-2] + "." + listTemp[-1]
                if lowLevel in dictTemp:
                    dictTemp[lowLevel] += num
                else:
                    dictTemp[lowLevel] = num
            if listTemp[-1] in dictTemp:
                dictTemp[listTemp[-1]] += num
            else:
                dictTemp[listTemp[-1]] = num

        # 遍历dict 输出list
        outList = []
        for key,value in dictTemp.items():
            outList.append(str(value) + " " + key)

        # print(outList)
        return outList
        pass

    # list 矩阵转换
    def transpose(self, A: list) -> list:
        print("func transpose")
        # print("    Sloution1:")
        # print("        Runtime: 76 ms, faster than 26.13% of Python3 online submissions for Transpose Matrix.")
        # print("        Memory Usage: 13.7 MB, less than 5.45% of Python3 online submissions for Transpose Matrix.")
        return (list(map(list, zip(*A))))

    def middleNode(self, head: ListNode) -> ListNode:
        print("func middleNode")
        # print("    Sloution1:")
        # print("        Runtime: 48 ms, faster than 20.29% of Python3 online submissions for Middle of the Linked List.")
        # print("        Memory Usage: 13.2 MB, less than 5.04% of Python3 online submissions for Middle of the Linked List.")
        # 快慢指针
        fast = slow = head
        # 遍历fast指针移动是slow两倍
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def increasingBST(self, root: TreeNode) -> TreeNode:
        print("func increasingBST")
        # print("    Sloution1:")
        # print("        Runtime: 176 ms, faster than 20.27% of Python3 online submissions for Increasing Order Search Tree.")
        # print("        Memory Usage: 13.4 MB, less than 5.97% of Python3 online submissions for Increasing Order Search Tree.")
        outList = []

        # 中序遍历数据到list
        def loopNode(node: TreeNode):
            if node:
                loopNode(node.left)
                # print(node.val)
                outList.append(node.val)
                loopNode(node.right)
        loopNode(root)

        def listToNode(node:TreeNode, listNode):
            while listNode:
                node.right = TreeNode(listNode[0])
                listNode.pop(0)
                listToNode(node.right, listNode)

        # 迭代 list转二叉树
        lenOutList = len(outList)
        outNode = TreeNode(outList[0])
        if lenOutList > 1:
            outList.pop(0)
            outNode.right = TreeNode(outList[0])
            outList.pop(0)
            listToNode(outNode.right, outList)
        print(outNode)
        return outNode

    # list逆序
    def reverseString(self, s: list) -> None:
        print("func reverseString")
        # print("    Sloution1:")
        # print("        Runtime: 184 ms")
        # print("        Memory Usage: 17.9 MB")
        # j = -1
        # for i in range(len(s) // 2):
        #     s[i], s[j] = s[j], s[i]
        #     j -= 1

        # print("    Sloution2:")
        # print("        Runtime: 196 ms, faster than 21.96% of Python3 online submissions for Reverse String.")
        # print("        Memory Usage: 17.7 MB, less than 11.40% of Python3 online submissions for Reverse String.")
        s.reverse()

        print(s)

    #
    def shortestToChar(self, S: str, C: str) -> list:

        print("func shortestToChar")
        # print("    Sloution1:")
        # print("        Runtime: 52 ms, faster than 74.08% of Python3 online submissions for Shortest Distance to a Character.")
        # print("        Memory Usage: 13.3 MB, less than 5.56% of Python3 online submissions for Shortest Distance to a Character.")
        matchList = []
        # 遍历确定C位置
        for i in range(len(S)):
            if S[i] == C:
                matchList.append(i)
        # print(matchList)

        outList = []
        # 对比第一个
        for i in range(0, matchList[0] + 1):
            outList.append(matchList[0] - i)

        # 对比中段
        j = 1
        for i in range(matchList[0] + 1, matchList[-1] + 1):
            if matchList[j] < i:
                j += 1
            outList.append(min(matchList[j] - i, i - matchList[j - 1]))


        # 对比最后一个
        for i in range( matchList[-1] + 1, len(S)):
            outList.append(i - matchList[-1])

        print(outList)
        return outList

    # 求从L到R 素数个数
    def countPrimeSetBits(self, L: int, R: int) -> int:
        print("func countPrimeSetBits")
        # print("    Sloution1:")
        # print("        Runtime: 604 ms, faster than 38.98% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.")
        # print("        Memory Usage: 13.1 MB, less than 5.55% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.")
        # R 不大于1M，说明最多有24个1，穷举素数字典
        # primeDict = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1, 23:1}
        #
        # primeNum = 0
        # for data in range(L, R + 1):
        #     binData = bin(data)[2:]
        #     tempCount = 0
        #     # 遍历统计1个数
        #     for str in binData:
        #         if str == "1":
        #             tempCount += 1
        #     # 判断是否属于素数
        #     if tempCount in primeDict:
        #         primeNum += 1
        #
        # # print(primeNum)
        # return primeNum

        # print("    Sloution2:")
        # print("        Runtime: 168 ms, faster than 98.78% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.")
        # print("        Memory Usage: 13.3 MB, less than 5.55% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.")
        # R 不大于1M，说明最多有24个1，穷举素数字典
        primeDict = {2, 3, 5, 7, 11, 13, 17, 19, 23}
        primeNum = 0
        for data in range(L, R + 1):
            # 判断是否属于素数 利用count计算
            if bin(data).count("1") in primeDict:
                primeNum += 1

        # print(primeNum)
        return primeNum


    def run(self):

        startTime = time.time()

        # self.postorder(self.node1)
        # self.preorder(self.node1)
        # self.projectionArea([[2,2,2],[2,1,3],[2,2,2]])
        # self.maxDepth(self.node1)
        # self.smallestRangeI([1,6,3], 2)
        # self.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
        # self.transpose([[1,2,3],[4,5,6]])
        # self.middleNode(self.listNode)
        # self.increasingBST(self.t1)
        # self.reverseString(["h","e","l","l","o"])
        # self.shortestToChar("loveleetcode", "e")
        self.countPrimeSetBits(6,10)
        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

