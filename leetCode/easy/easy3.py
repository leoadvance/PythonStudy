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

        self.listNode = ListNode(1)
        self.listNode.next = ListNode(2)
        self.listNode.next.next = ListNode(3)
        self.listNode.next.next.next = ListNode(4)
        self.listNode.next.next.next.next = ListNode(5)
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

    def run(self):

        startTime = time.time()

        # self.postorder(self.node1)
        # self.preorder(self.node1)
        # self.projectionArea([[2,2,2],[2,1,3],[2,2,2]])
        # self.maxDepth(self.node1)
        # self.smallestRangeI([1,6,3], 2)
        # self.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
        # self.transpose([[1,2,3],[4,5,6]])
        self.middleNode(self.listNode)
        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

