# coding=utf-8
import re
import time
import collections
import operator
from typing import List


class SolutionEasy():

    def __init__(self):

        print("class leetCode SolutionEasy init!")


    def __del__(self):
        print("class leetCode SolutionEasy delete!")

    def largestPerimeter(self, A: list) -> int:
        print("func largestPerimeter")
        # print("    Sloution1:")
        # print("        Runtime: 72 ms, faster than 98.12% of Python3 online submissions for Largest Perimeter Triangle.")
        # print("        Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Largest Perimeter Triangle.")

        # 降序排列
        A.sort(reverse = True)

        # 遍历 利用三角形两边之和大于第三边来判断
        for i in range(len(A) - 2):
            # 两边和大于第三边
            if A[i] < A[i + 1] + A[i + 2]:
                print(sum(A[i: i + 3]))
                return sum(A[i: i + 3])

        print(0)
        return 0

    # 判断一个数字是否被5整除
    def prefixesDivBy5(self, A: list) -> list:
        print("func largestPerimeter")
        # print("    Sloution1:")
        # print("        Runtime: 112 ms, faster than 100.00% of Python3 online submissions for Binary Prefix Divisible By 5.")
        # print("        Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Binary Prefix Divisible By 5.")
        outList = []
        sum = 0
        for data in A:
            # 利用除法特性 直接用余数迭代
            sum = ((sum << 1 ) + data) % 5
            if sum == 0:
                outList.append(True)
            else:
                outList.append(False)

        # print(outList)
        return outList

    # 交换数组中某元素 使其和相等
    def fairCandySwap(self, A: list, B: list) -> list:
        print("func fairCandySwap")
        # print("    Sloution1:")
        # print("        Runtime: 2568 ms, faster than 19.20% of Python3 online submissions for Fair Candy Swap.")
        # print("        Memory Usage: 14.4 MB, less than 51.52% of Python3 online submissions for Fair Candy Swap.")

        # # 算出差值
        # Delta = (sum(A) - sum(B)) >> 1
        #
        # for data in A:
        #     if (data - Delta) in B:
        #         print([data, data - Delta])
        #         return [data, data - Delta]

        # print("    Sloution2:")
        # print("        Runtime: 80 ms, faster than 54.31% of Python3 online submissions for Fair Candy Swap.")
        # print("        Memory Usage: 15.4 MB, less than 5.05% of Python3 online submissions for Fair Candy Swap.")

        # 算出差值
        Delta = (sum(A) - sum(B)) >> 1
        B = set(B)
        for data in A:
            if (data - Delta) in B:
                print([data, data - Delta])
                return [data, data - Delta]

    # 判断a序列中最长不包含在B系列中的数据长度
    def findLUSlength(self, a: str, b: str) -> int:

        # 特别无聊的题目 不知道出题人想要干嘛
        if a == b:
            return -1
        return max(len(a), len(b))
        pass

    # 删除最外层括号
    def removeOuterParentheses(self, S: str) -> str:
        out = ""
        sign = 0
        for data in S:
            if data == "(":
                if sign != 0:
                    out += data
                sign += 1
            # ")"
            else:
                if sign > 1:
                    out += data
                sign -= 1
        print(out)
        return out
        pass

    #
    def camelMatch(self, queries: list, pattern: str) -> list:
        patternList = []
        outList = []
        # 从大写字符开始
        temp = ""
        for i in range(len(pattern)):
            if ord(pattern[i]) < ord("a"):
                temp = pattern[i]
                break
        i += 1
        for data in pattern[i:]:
            if ord(data) < ord("a"):
                if temp:
                    patternList.append(collections.Counter(temp))
                temp = data

            else:
                temp += data
        # 拆分成不同大写开始的段
        patternList.append(collections.Counter(temp))
        # print(patternList)

        # 遍历
        for strs in queries:
            tempList = []
            # 从大写字符开始
            for i in range(len(strs)):
                if ord(strs[i]) < ord("a"):
                    temp = strs[i]
                    break
            i += 1
            for data in strs[i:]:
                if ord(data) < ord("a"):
                    if temp:
                        tempList.append(collections.Counter(temp))
                    temp = data

                else:
                    temp += data

            tempList.append(collections.Counter(temp))
            # 分段不等一定不等
            if len(tempList) != len(patternList):
                outList.append(False)
            else:
                sign = 0
                for i in range(len(tempList)):
                    for key, val in patternList[i].items():
                        if val > tempList[i][key]:
                            outList.append(False)
                            sign = 1
                            break
                    if sign == 1:
                        break
                if sign == 0:
                    outList.append(True)
        #     print(tempList)
        # print(outList)
        return outList

    # 字符倒序
    def reverseOnlyLetters(self, S: str) -> str:
        print("func reverseOnlyLetters")
        # print("    Sloution1:")
        # print("        Runtime: 36 ms, faster than 91.24% of Python3 online submissions for Reverse Only Letters.")
        # print("        Memory Usage: 13.2 MB, less than 5.56% of Python3 online submissions for Reverse Only Letters.")
        # str转list
        listS = list(S)
        outList = [0 for i in range(len(S))]
        # print(listS)
        j = len(S) - 1
        i = 0
        # 从头尾两端遍历
        while(i <= j):

            # 遇到非字母则跳过进行下一个数据交换
            if S[i].isalpha() == False:
                outList[i] = S[i]
                i += 1
                continue

            if S[j].isalpha() == False:
                outList[j] = S[j]
                j -= 1
                continue

            outList[i], outList[j] = S[j], S[i]
            i += 1
            j -= 1
        outStr = "".join(outList)
        print(outStr)
        return outStr

    def lemonadeChange(self, bills: List[int]) -> bool:
        print("func lemonadeChange")
        # print("    Sloution1:")
        # print("        Runtime: 48 ms, faster than 88.01% of Python3 online submissions for Lemonade Change.")
        # print("        Memory Usage: 13.2 MB, less than 6.15% of Python3 online submissions for Lemonade Change.")
        change5 = 0
        change10 = 0
        for data in bills:
            if data == 5:
                change5 += 1
            if data == 10:
                if change5 > 0:
                    change5 -= 1
                    change10 += 1
                else:
                    print(False)
                    return False
            if data == 20:
                if  change5 > 0 and change10 > 0:
                    change10 -= 1
                    change5 -= 1
                elif change5 > 2:
                    change5 -= 3

                else:
                    print(False)
                    return False

        print(True)
        return True

    def isMonotonic(self, A: List[int]) -> bool:

        print("func isMonotonic")
        # print("    Sloution1:")
        # print("        Runtime: 84 ms, faster than 96.13% of Python3 online submissions for Monotonic Array.")
        # print("        Memory Usage: 17.3 MB, less than 5.11% of Python3 online submissions for Monotonic Array.")
        total = 2

        # 递减判断
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                total -= 1
                break
        # 递增判断
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                total -= 1
                break

        if total >= 1:
            print(True)
            return True
        else:
            print(False)
            return False

        pass

    # 判断波峰波谷
    def maxProfit(self, prices: List[int]) -> int:
        print("func maxProfit")
        # print("    Sloution1:")
        # print("        Runtime: 56 ms, faster than 17.77% of Python3 online submissions for Best Time to Buy and Sell Stock II.")
        # print("        Memory Usage: 14.1 MB, less than 5.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.")
        # haveStock = 0
        # sum = 0
        # for i in range(len(prices) - 1):
        #     # 没有股票 准备买入
        #     if haveStock == 0:
        #         # 波谷买入
        #         if prices[i + 1] > prices[i]:
        #             currentPrice = prices[i]
        #             haveStock    = 1
        #     else:
        #         # 波峰卖出
        #         if prices[i + 1] < prices[i]:
        #             sum += prices[i] - currentPrice
        #             haveStock = 0
        # # 最后一次卖出
        # if haveStock == 1:
        #     sum += prices[-1] - currentPrice
        #
        # print(sum)
        # return sum
        print("    Sloution2:")
        # print("        Runtime: 40 ms, faster than 98.98% of Python3 online submissions for Best Time to Buy and Sell Stock II.")
        # print("        Memory Usage: 14.1 MB, less than 5.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.")
        sum = 0
        for i in range(1, len(prices)):
            # 低买高卖
            if prices[i] > prices[i-1]:
                sum += prices[i] - prices[i-1]

        print(sum)
        return sum

        pass

    def run(self):

        startTime = time.time()

        # self.largestPerimeter([3,6,2])
        # self.prefixesDivBy5([0,1,1,1,1,1])

        # self.fairCandySwap([2], [1,3])
        # self.findLUSlength("aba", "cdc")
        # self.removeOuterParentheses("()()")
        # self.camelMatch(["mifeqvzphnrv","mieqxvrvhnrv","mhieqovhnryv","mieqekvhnrpv","miueqrvfhnrv","mieqpvhzntrv","gmimeqvphnrv","mieqvhqyunrv"],"mieqvhnrv")
        # self.reverseOnlyLetters("Test1ng-Leet=code-Q!")
        # self.lemonadeChange([5,5,10,10,20])
        # self.isMonotonic([6,5,4,4])
        self.maxProfit([7,1,5,3,6,4])

        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

