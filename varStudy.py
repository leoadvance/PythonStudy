# coding=utf-8


class VariableClass():

    def __init__(self):
        print("class varibale init!")

    def __del__(self):
        print("class varibale delete!")

    # int型数据应用学习
    def intStudy(self) -> int:
        print("\n\nint型学习")
        intA  = 1
        intA += 1
        print("                intA Type: ", type(intA), " value: ", intA)
        return intA

    def floatStufy(self, intA:int = 1)  -> float:
        print("\n\nfloat型学习")
        floatA = (float)(intA)
        print("                floatA Type: ", type(floatA), " value: ", floatA)
        return floatA

    def run(self):

        intA = self.intStudy()

        floatA = self.floatStufy(intA)

        strA = (str)(floatA)
        strB = "asdasd"
        strC = strA + strB


        print("                strA Type: ", type(strA), " value: ", strA, "strB = \"asdasd\"", "strC = (strA + strB) =  ", strC, "strC[2:5] = ", strC[2:5])
        pass