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





class SolutionEasy():

    def __init__(self):
        print("class leetCode SolutionEasy init!")
        self.q = collections.deque()

    def __del__(self):
        print("class leetCode SolutionEasy delete!")

    def minDeletionSize(self, A: list) -> int:
        print("func minDeletionSize")
        # print("    Sloution1:")
        # print("        Runtime: 224 ms, faster than 27.37% of Python3 online submissions for Delete Columns to Make Sorted.")
        # print("        Memory Usage: 15.1 MB, less than 5.45% of Python3 online submissions for Delete Columns to Make Sorted.")
        # compareCount = len(A)
        # totalCount   = 0
        # result = [[0 for i in range(len(A[0]))] for j in range(compareCount)]
        # for i in range(compareCount):
        #     result[i] = list(A[i])
        # # print(result)
        # result = list(map(list, zip(*result)))
        # # print(result)
        #
        # for listTemp in result:
        #     for i in range(compareCount - 1):
        #         if listTemp[i] > listTemp[i + 1]:
        #             totalCount += 1
        #             break
        #
        # print(totalCount)
        # return totalCount

        # print("    Sloution2:")
        # print("        Runtime: 164 ms, faster than 55.56% of Python3 online submissions for Delete Columns to Make Sorted.")
        # print("        Memory Usage: 14.5 MB, less than 5.45% of Python3 online submissions for Delete Columns to Make Sorted.")
        # compareCount = len(A)
        # totalCount   = 0
        # result = [list(i) for i in A]
        # result = zip(*result)
        # # print(result)
        #
        # for listTemp in result:
        #     for i in range(compareCount - 1):
        #         if listTemp[i] > listTemp[i + 1]:
        #             totalCount += 1
        #             break
        #
        # print(totalCount)
        # return totalCount

        # 1 主要学习zip进行list横纵交换 copy复制以及sort排序
        print("    Sloution3:")
        print("        Runtime: 120 ms, faster than 87.36% of Python3 online submissions for Delete Columns to Make Sorted.")
        print("        Memory Usage: 13.9 MB, less than 6.36% of Python3 online submissions for Delete Columns to Make Sorted.")
        zipped = zip(*A)
        totalCount   = 0
        # print(zipped)

        for listTemp in zipped:
            listTemp = list(listTemp)
            listTemp2 = listTemp.copy()
            listTemp.sort()
            if listTemp2 != listTemp:
                totalCount += 1

        # print(totalCount)
        return totalCount

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

    # 求list里数据最大值
    def peakIndexInMountainArray(self, A: list) -> int:
        print("func peakIndexInMountainArray")
        # print("    Sloution1:")
        # print("        Runtime: 60 ms, faster than 16.07% of Python3 online submissions for Peak Index in a Mountain Array.")
        # print("        Memory Usage: 14.3 MB, less than 5.42% of Python3 online submissions for Peak Index in a Mountain ")
        # i = 1
        # while(i < len(A) - 1):
        #     if A[i] >  A[i - 1] and A[i] < A[i + 1]:
        #         return i
        #
        #     print(A[i])
        #     i += 1
        # return 0
        print("    Sloution2:")
        print("        Runtime: 40 ms, faster than 69.63% of Python3 online submissions for Peak Index in a Mountain Array.")
        print("        Memory Usage: 14 MB, less than 5.42% of Python3 online submissions for Peak Index in a Mountain Array.")
        # print(A.index(max(A)))
        return A.index(max(A))

    def ping(self, t: int) -> int:
        # print("func ping")
        # print("    Sloution1:")
        # print("        Runtime: 256 ms, faster than 42.04% of Python3 online submissions for Number of Recent Calls.")
        # print("        Memory Usage: 18 MB, less than 5.71% of Python3 online submissions for Number of Recent Calls.")
        # self.list.append(t)
        # t -= 3000
        # temp = 0
        # for data in self.list:
        #     # print("data = ", data)
        #     if data < t:
        #         # print("data = ", data, "list before=", self.list, "t = ",t)
        #         temp += 1
        #         # print("data = ", data, "list=", self.list)
        #     else:
        #         for i in range(temp):
        #             self.list.pop(0)
        #         break
        # # print("self.list", self.list, "len :", len(self.list))
        # return len(self.list)
        # print("    Sloution2:")
        # print("        Runtime: 212 ms, faster than 56.99% of Python3 online submissions for Number of Recent Calls.")
        # print("        Memory Usage: 17.6 MB, less than 5.71% of Python3 online submissions for Number of Recent Calls.")
        # self.list.append(t)
        # t -= 3000
        # while(self.list[0] < t):
        #
        #     self.list.pop(0)
        #
        # print("self.list", self.list, "len :", len(self.list))
        # return len(self.list)
        # print("    Sloution3:")
        # print("        Runtime: 200 ms, faster than 71.17% of Python3 online submissions for Number of Recent Calls.")
        # print("        Memory Usage: 17.9 MB, less than 5.71% of Python3 online submissions for Number of Recent Calls.")
        self.q.append(t)
        t -= 3000
        while(self.q[0] < t):

            self.q.popleft()

        # print("self.q", self.q, "len :", len(self.q))
        return len(self.q)

    def commonChars(self, A: list) -> list:

        print("func commonChars")
        # print("    Sloution1:")
        # print("        Runtime: 60 ms, faster than 79.19% of Python3 online submissions for Find Common Characters.")
        # print("        Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Find Common Characters.")
        # multList = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        # outList = []
        # LISTLEN = len(A)
        # # print(multList)
        # for i in range(LISTLEN):
        #     multList[i] = list(A[i])
        # # print(multList)
        #
        # for char in multList[0]:
        #     mark = 0
        #     # print("char = ", char)
        #     for j in range(1, LISTLEN):
        #         if char in multList[j]:
        #             multList[j].remove(char)
        #             # print("multList ", j, multList[j])
        #         else:
        #             mark = 1
        #             break
        #     if mark == 0:
        #         outList.append(char)
        #
        # print(outList)
        # return outList

        print("    Sloution2:")
        print("        Runtime: 48 ms, faster than 98.53% of Python3 online submissions for Find Common Characters.")
        print("        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Common Characters.")
        outList = []

        # collections.Counter 创建dict并对不同元素计数
        dictTemp = dict(collections.Counter(A[0]))
        # print(dictTemp)

        for k, v in dictTemp.items():
            flag     = True
            minValue = v
            for i in range(1, len(A)):
                if k not in A[i]:
                    flag = False
                    break
                else:
                    minValue = min(minValue, A[i].count(k))

            if flag:
                # print([k] * minValue)
                outList.extend([k] * minValue)
        print(outList)
        return outList

    def sumEvenAfterQueries(self, A: list, queries) -> list:

        print("func sumEvenAfterQueries")
        print("    Sloution1:")
        print("        Runtime: 176 ms, faster than 47.81% of Python3 online submissions for Sum of Even Numbers After Queries.")
        print("        Memory Usage: 17.5 MB, less than 5.56% of Python3 online submissions for Sum of Even Numbers After Queries.")
        # 算出初始值
        sum = 0
        for data in A:
            if data % 2 == 0:
                sum += data

        outList = []
        for v,p in queries:
            # print(v,p)

            # 待处理是偶数
            if v % 2 == 0:
                # 原数也是偶数
                if A[p] % 2 == 0:
                    # 更新数据
                    sum += v
            else:
                # 原数是偶数
                if A[p] % 2 == 0:
                    # 更新数据
                    sum -= A[p]

                else:
                    sum += v+A[p]

            A[p] += v
            outList.append(sum)
        print(outList)
        return outList

    def run(self):

        startTime = time.time()
        # self.minDeletionSize(["cba","daf","ghi"])
        # t1 = TreeNode(1)
        # t1.left  = TreeNode(3)
        # t1.right = TreeNode(2)
        # t1.left.left = TreeNode(5)
        # t1.left.right = TreeNode(6)
        #
        # t2 = TreeNode(1)
        # t2.left  = TreeNode(1)
        # t2.right = TreeNode(3)
        # t2.left.right = TreeNode(4)
        # t2.right.right = TreeNode(7)
        # self.mergeTrees(t1, t2)
        # self.peakIndexInMountainArray([0,2,1,0])
        # listTemp = [[642],[1849],[4921],[5936],[5957]]
        #
        # for i in listTemp:
        #     self.ping(i[0])
        # self.commonChars(["bella","label","roller"])
        self.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]])
        endTime = time.time()
        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

