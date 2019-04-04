# coding=utf-8
import re
import time
import collections

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionMedium():

    def __init__(self):
        self.list = ListNode(1)
        self.list.next = ListNode(7)
        self.list.next.next = ListNode(5)
        self.list.next.next.next = ListNode(1)
        self.list.next.next.next.next = ListNode(9)
        self.list.next.next.next.next.next = ListNode(2)
        self.list.next.next.next.next.next.next = ListNode(5)
        self.list.next.next.next.next.next.next.next = ListNode(1)
        print("class leetCode SolutionMedium1 init!")

    def __del__(self):
        print("class leetCode SolutionMedium1 delete!")


    def smallestRepunitDivByK(self, K: int) -> int:
        # print("func smallestRepunitDivByK")
        # print("    Sloution1:")
        # print("        Runtime: 1032 ms, faster than 100.00% of Python3 online submissions for Smallest Integer Divisible by K.")
        # print("        Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Smallest Integer Divisible by K.")
        # 偶数不可能被n个1整除 5也不会
        if K % 2 == 0 or K == 5:
            # print(-1)
            return -1

        tempLen = 0
        value = 0
        # 遍历 模拟除法 用余数进位后+1 进入下一轮
        for i in range(10 ** 6):
            tempLen += 1
            value = (value * 10 + 1) % K
            if value % K == 0:
                print(tempLen)
                return tempLen


        return -1

    # 求两list数据两两相加最小值
    def maxScoreSightseeingPair(self, A: list) -> int:
        # print("func maxScoreSightseeingPair")
        # print("    Sloution1:")
        # print("        Runtime: 208 ms, faster than 32.53% of Python3 online submissions for Best Sightseeing Pair.")
        # print("        Memory Usage: 19.6 MB, less than 100.00% of Python3 online submissions for Best Sightseeing Pair.")
        # 偶数不可能被n个1整除 5也不会
        # iList = A + i  jList = A - J
        # iList = [A[i] + i for i in range(len(A) - 1)]
        # jList = [A[j] - j for j in range(1, len(A))]
        # print(A)
        # print(iList)
        # print(jList)
        #
        # # 遍历 逆序遍历jList各个位置最大值
        # i = -1
        # maxjlist  = -100000
        # maxResult = -100000
        # for data in jList[::-1]:
        #     maxjlist  = max(maxjlist, data)
        #     maxResult = max(maxResult, maxjlist + iList[i])
        #     print("maxjlist", maxjlist," iList[i]", iList[i])
        #     i -= 1
        #     # print(data)
        #
        # print(maxResult)
        # return maxResult

        # print("    Sloution2:")
        # print("        Runtime: 188 ms, faster than 45.55% of Python3 online submissions for Best Sightseeing Pair.")
        # print("        Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Best Sightseeing Pair.")
        maxiList  = A[0]
        maxResult = -1000000
        for i in range(1, len(A)):

            # 更新maxiList + A[i] - i 最大值
            maxResult = max(maxResult, maxiList + A[i] - i)

            # 更新A[i] + i最大值
            maxiList  = max(maxiList, A[i] + i)
            # print("maxiList", maxiList, " maxResult", maxResult)

        # print(maxResult)
        return maxResult


    # 十进制数转换成基于-2的二进制数
    def baseNeg2(self, N: int) -> str:
        print("func largestPerimeter")
        # print("    Sloution1:")
        # print("        Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Convert to Base -2.")
        # print("        Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Convert to Base -2.")
        # N < 10^9 所以数据不会大于2^33
        sign = [1 << i for i in range(1, 33, 2)]
        # print(sign)

        for mark in sign:
            # 如果N中对应的mark位置位，则用 2^(n - 1) = (-2)^n + (-2)^(n-1) 如 2 = 4 - 2
            if N & mark:
                N += mark << 1
        # print(bin(N)[2:])
        return bin(N)[2:]

    # 求list里每个数字下一个最大值
    def nextLargerNodes(self, head: ListNode) -> list:
        print("func nextLargerNodes")
        # print("    Sloution1:")
        # print("        Runtime: 412 ms, faster than 87.32% of Python3 online submissions for Next Greater Node In Linked List.")
        # print("        Memory Usage: 17.7 MB, less than 100.00% of Python3 online submissions for Next Greater Node In Linked List.")
        # listNode转list
        queue = []
        while head:
            queue.append(head.val)
            head = head.next
        # print(queue)


        res = [0 for i in range(len(queue))]
        stack = []

        # 逆向遍历list
        for i in range(len(queue) - 1, -1, -1):

            # 从右往左删除堆栈中比当前数字小的数字，剩下的就是第一个比当前数字大的数字
            while stack and queue[i] >= queue[stack[-1]]:
                stack.pop()
            # 保存该（大的）数据到输出列表
            if stack:
                res[i] = queue[stack[-1]]

            # 添加最新数据到堆栈
            stack.append(i)

        return res
        pass

    def queryString(self, S: str, N: int) -> bool:
        pass

    # 行列最大值
    def maxIncreaseKeepingSkyline(self, grid: list) -> int:
        print("func maxIncreaseKeepingSkyline")
        # print("    Sloution1:")
        # print("        Runtime: 48 ms, faster than 82.85% of Python3 online submissions for Max Increase to Keep City Skyline.")
        # print("        Memory Usage: 12.9 MB, less than 5.55% of Python3 online submissions for Max Increase to Keep City Skyline.")
        # 获取行列最大值
        maxRow    = [max(grid[i]) for i in range(len(grid))]
        maxColumn = []
        totalCount = 0
        for j in range(len(grid)):
            maxTemp = 0
            for i in range(len(grid[0])):
                maxTemp = max(maxTemp, grid[i][j])
            maxColumn.append(maxTemp)

        # print(maxColumn)
        # print(maxRow)

        # 遍历 取该点行列最大值的较小值，并与原始值求查 并累计
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                totalCount += min(maxRow[i],maxColumn[j]) - grid[i][j]
        # print(totalCount)
        return totalCount
        pass

    # 按要求变换list
    def deckRevealedIncreasing(self, deck: list) -> list:
        print("func deckRevealedIncreasing")
        # print("    Sloution1:")
        # print("        Runtime: 44 ms, faster than 90.66% of Python3 online submissions for Reveal Cards In Increasing Order.")
        # print("        Memory Usage: 13.4 MB, less than 5.80% of Python3 online submissions for Reveal Cards In Increasing Order.")
        # 获取行列最大值
        # 采用双向链表处理
        outList = collections.deque()

        # 先升序准备好要遍历数列
        deck.sort()
        outList.append(deck[-1])

        # 根据翻牌规格 每次把数组最后一个数放到最前 并添加list数据到链表第一位
        for data in deck[-2::-1]:
            outList.appendleft(outList.pop())
            outList.appendleft(data)
            # print(data)
        print(outList)
        return list(outList)
        pass

    def run(self):

        startTime = time.time()
        # self.smallestRepunitDivByK(7)
        # self.maxScoreSightseeingPair([1,1,1])
        # self.baseNeg2(13)
        # self.nextLargerNodes(self.list)
        # self.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
        self.deckRevealedIncreasing([17,13,11,2,3,5,7])

        endTime = time.time()
        print("leetCode SolutionMedium1 run time: ", (str(endTime - startTime))[:8], "s")

        pass

