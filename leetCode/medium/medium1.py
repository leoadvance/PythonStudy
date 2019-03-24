# couding=utf-8
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


    def run(self):

        startTime = time.time()
        self.smallestRepunitDivByK(7)
        endTime = time.time()
        print("leetCode SolutionMedium1 run time: ", (str(endTime - startTime))[:8], "s")

        pass

