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

    def run(self):
        self.numJewelsInStones("aA", "aAAbbbb")
        pass