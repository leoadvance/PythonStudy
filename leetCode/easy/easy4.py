# coding=utf-8
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

    def numSpecialEquivGroups(self, A: list) -> int:
        print("func numSpecialEquivGroups")
        # print("    Sloution1:")
        # print("        Runtime: 52 ms, faster than 50.95% of Python3 online submissions for Groups of Special-Equivalent Strings.")
        # print("        Memory Usage: 13.6 MB, less than 6.38% of Python3 online submissions for Groups of Special-Equivalent Strings.")
        # 遍历字符串，记录26个字母在奇偶位置出现次数
        # def count(A):
        #     ans = [0] * 52
        #     for i, letter in enumerate(A):
        #         ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
        #     return tuple(ans)
        # # 利用字典key不重复特性统计不同组合情况
        # return len({count(word) for word in A})

        # print("    Sloution2:")
        # print("        Runtime: 44 ms, faster than 81.30% of Python3 online submissions for Groups of Special-Equivalent Strings.")
        # print("        Memory Usage: 13.2 MB, less than 6.38% of Python3 online submissions for Groups of Special-Equivalent Strings.")
        # 遍历字符串，记录26个字母在奇偶位置出现次数
        outData = set()
        for string in A:
            # 利用sorted和字符串slice功能分离奇偶字符串
            even = sorted(string[::2])
            odd  = sorted(string[1::2])
            # print(even,odd)

            # 利用set唯一性添加元素
            outData.add("".join(even) + "".join(odd))
        print(outData)
        return len(outData)

    def uncommonFromSentences(self, A: str, B: str) -> list:
        print("func uncommonFromSentences")
        # print("    Sloution1:")
        # print("        Runtime: 40 ms, faster than 54.75% of Python3 online submissions for Uncommon Words from Two Sentences.")
        # print("        Memory Usage: 13.3 MB, less than 5.71% of Python3 online submissions for Uncommon Words from Two Sentences.")
        # 利用collections.Counter和split生成字典 并合并同类项
        # dictA = dict(collections.Counter(A.split(" ")))
        # dictB = dict(collections.Counter(B.split(" ")))
        #
        # for k,v in dictB.items():
        #     if k in dictA:
        #         dictA[k] += v
        #     else:
        #         dictA[k] = v
        # # print(dictA, dictB)
        #
        # # 遍历 输出只有单个val的key
        # outlist = []
        # for k,v in  dictA.items():
        #     if v == 1:
        #         outlist.append(k)
        #
        # # print(outlist)
        # return outlist

        # print("    Sloution2:")
        # print("        Runtime: 40 ms, faster than 54.75% of Python3 online submissions for Uncommon Words from Two Sentences.")
        # print("        Memory Usage: 13 MB, less than 5.71% of Python3 online submissions for Uncommon Words from Two Sentences.")

        # 利用collections.Counter和split生成字典 并合并同类项
        dictA = collections.Counter(A.split(" ")) + collections.Counter(B.split(" "))

        print(type(dictA))

        # 遍历 输出只有单个val的key
        outlist = []
        for k,v in  dictA.items():
            if v == 1:
                outlist.append(k)

        print(outlist)
        return outlist

    def calPoints(self, ops: list) -> int:
        print("func calPoints")
        # print("    Sloution1:")
        # print("        Runtime: 40 ms, faster than 57.63% of Python3 online submissions for Baseball Game.")
        # print("        Memory Usage: 13.1 MB, less than 5.15% of Python3 online submissions for Baseball Game.")
        # 遍历并按要求转换
        tempList = []
        for s in ops:
            # 如果是C 删除最后一个元素
            if s == "C":
                tempList.pop()

            # 是D有效数据翻倍
            elif s == "D":
                tempList.append(tempList[-1] * 2)
            # 遇到➕ 最后两个有效数据相加
            elif s == "+":
                tempList.append(tempList[-1] + tempList[-2])
            # 字符转数字
            else:
                tempList.append(int(s))
        print(tempList, sum(tempList))
        return sum(tempList)

    # 判断周长
    def islandPerimeter(self, grid) -> int:
        print("func calPoints")
        # print("    Sloution1:")
        # print("        Runtime: 380 ms, faster than 34.42% of Python3 online submissions for Island Perimeter.")
        # print("        Memory Usage: 13.4 MB, less than 6.11% of Python3 online submissions for Island Perimeter.")
        tempTuple = ((-1,0), (1,0), (0, -1), (0, 1))
        # 声明空二维数组
        templist = [[0] * (len(grid[0]) + 2) for i in range(len(grid) + 2)]
        print(templist)

        # 旧数组合并到新数组
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                templist[i + 1][j + 1] = grid[i][j]
        sum = 0
        for i in range(1, len(templist) - 1):
            for j in range(1, len(templist[0]) -1):
                # 是否陆地
                if (templist[i][j] > 0):
                    sum += 4

                    # 判断前后左右是否有陆地 有则相邻边减一
                    for a,b in tempTuple:
                        if templist[i + a][j + b] > 0:
                            sum -= 1
        print(templist, sum)
        return sum
        pass

    # 求list内是否可以分成3组和相等的数
    def canThreePartsEqualSum(self, A: list) -> bool:

        # 和相等 说明每个都是总和的三分之一
        tempSign = sum(A) / 3
        # print(tempSign)
        tempSum = 0
        tempCount = 0

        # 遍历，统计和等于三分之一总和的次数
        for i in range(len(A)):
            tempSum += A[i]

            # 得到第一个平均值
            if tempSum == tempSign:
                tempSum = 0
                tempCount += 1

        if tempCount == 3 and tempSum == 0:
            print(True)
            return True
        else:
            print(False)
            return False

        pass

    # 找出二进制中两个1之间最远距离
    def binaryGap(self, N: int) -> int:
        print("func binaryGap")
        # print("    Sloution1:")
        # print("        Runtime: 36 ms, faster than 99.25% of Python3 online submissions for Binary Gap.")
        # print("        Memory Usage: 13.1 MB, less than 6.67% of Python3 online submissions for Binary Gap.")
        # int转2进制
        dataStrings = bin(N)[3:]
        maxLen = 1
        currentLen = 0
        oneCount = 1
        # 遍历 相邻1间隔
        for strData in dataStrings:
            currentLen += 1

            if strData == "1":
                oneCount += 1
                if currentLen != 0:
                    maxLen = max(maxLen, currentLen)
                    currentLen = 0
        if (oneCount == 1):
            maxLen = 0
        print(maxLen,dataStrings)
        return maxLen

    def fizzBuzz(self, n: int) -> list:
        print("func binaryGap")
        # print("    fizzBuzz:")
        # print("        Runtime: 56 ms, faster than 62.22% of Python3 online submissions for Fizz Buzz.")
        # print("        Memory Usage: 14.1 MB, less than 5.17% of Python3 online submissions for Fizz Buzz.")
        outList = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                outList.append("FizzBuzz")
            elif i % 3 == 0:
                outList.append("Fizz")
            elif i % 5 == 0:
                outList.append("Buzz")
            else:
                outList.append(str(i))
        print(outList)
        return  outList

    def run(self):

        startTime = time.time()

        # self.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")
        # self.leafSimilar(self.t1, self.t2)
        # self.findComplement(5)
        # self.findWords(["Hello", "Alaska", "Dad", "Peace"])
        # self.numSpecialEquivGroups(["abcd","cdab","adcb","cbad"])
        # self.uncommonFromSentences("this apple is sweet", "this apple is sour")
        # self.calPoints(["5","-2","4","C","D","9","+","+"])
        # self.islandPerimeter([[1,0,0]])
        # self.binaryGap(2)
        self.fizzBuzz(15)

        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

