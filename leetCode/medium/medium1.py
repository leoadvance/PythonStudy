# couding=utf-8
import re
import time

class SolutionMedium():

    def __init__(self):
        print("class leetCode SolutionMedium1 init!")

    def __del__(self):
        print("class leetCode SolutionMedium1 delete!")


    def smallestRepunitDivByK(self, K: int) -> int:

        # 偶数不可能被n个1整除
        if K % 2 == 0 or K == 5:
            # print(-1)
            return -1

        tempLen = 0
        value = 0
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

