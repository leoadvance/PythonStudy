# couding=utf-8

class Sloution():

    def __init__(self):
        print("class leetCode sloution init!")

    def __del__(self):
        print("class leetCode sloution delete!")


    def numJewelsInStones(self, J: str, S: str) -> int:
        dictTemp = {}
        # 遍历字符串并转换成字典
        for s in S:
            if s in dictTemp:
                dictTemp[s] += 1
            else:
                dictTemp[s] = 1
        print("dictTemp:", dictTemp)
        result = 0
        for j in J:
            if j in dictTemp:
                result += dictTemp[j]
        print("func numJewelsInStones")
        print("    input string:")
        print("        J: ", J)
        print("        S: ", S)
        print("    output:")
        print("        Result = ", result)
        return result

    # 大小写转换
    def toLowerCase(self, str: str) -> str:

        print("func toLowerCase")
        print("    Sloution1:")
        print("        Runtime: 52 ms, Runtime: 52 ms, faster than 15.19% of Python3 online submissions for To Lower Case.")
        print("        Memory Usage: 13.1 MB, less than 5.45% of Python3 online submissions for To Lower Case.")
        liststr = list(str)
        for i in range(len(liststr)):

            if liststr[i] <= "Z" and liststr[i] >= "A":
                liststr[i] = (chr)((ord)(liststr[i]) + 32)
        # print(liststr)
        return "".join(liststr)
        # dictStr = {"A":"a","B":"b","C":"c"}
        # liststr = list(str)
        # for i in range(len(liststr)):
        #     if liststr[i] in dictStr:
        #         liststr[i]

    def run(self):
        # self.numJewelsInStones("aA", "aAAbbbb")
        self.toLowerCase("aHYebcd")
        pass