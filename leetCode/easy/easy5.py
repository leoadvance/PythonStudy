# coding=utf-8
import re
import time
import collections
import operator



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

    def run(self):

        startTime = time.time()

        # self.largestPerimeter([3,6,2])
        # self.prefixesDivBy5([0,1,1,1,1,1])

        self.fairCandySwap([2], [1,3])
        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

