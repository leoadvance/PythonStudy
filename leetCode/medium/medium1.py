# coding=utf-8
import re
import time

class SolutionMedium():

    def __init__(self):
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


    def queryString(self, S: str, N: int) -> bool:
        pass


    def run(self):

        startTime = time.time()
        # self.smallestRepunitDivByK(7)
        # self.maxScoreSightseeingPair([1,1,1])
        self.baseNeg2(13)
        endTime = time.time()
        print("leetCode SolutionMedium1 run time: ", (str(endTime - startTime))[:8], "s")

        pass

