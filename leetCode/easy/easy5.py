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

    def run(self):

        startTime = time.time()

        self.largestPerimeter([3,6,2])

        endTime = time.time()

        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

