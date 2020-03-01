# coding=utf-8
import re
import time
from typing import List

class SolutionEasy():

    def __init__(self):
        print("class leetCode SolutionEasy1 init!")

    def __del__(self):
        print("class leetCode SolutionEasy1 delete!")


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
        # print("    Sloution1:")
        # print("        Runtime: 52 ms, Runtime: 52 ms, faster than 15.19% of Python3 online submissions for To Lower Case.")
        # print("        Memory Usage: 13.1 MB, less than 5.45% of Python3 online submissions for To Lower Case.")
        # liststr = list(str)
        # for i in range(len(liststr)):
        #
        #     if liststr[i] <= "Z" and liststr[i] >= "A":
        #         liststr[i] = (chr)((ord)(liststr[i]) + 32)
        # # print(liststr)
        # return "".join(liststr)
        # print("    Sloution2:")
        # print("        Runtime: 52 ms, faster than 15.24% of Python3 online submissions for To Lower Case.")
        # print("        Memory Usage: 13.2 MB, less than 5.45% of Python3 online submissions for To Lower Case.")

        # dictStr = {"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g"
        #            ,"H":"h","I":"i","J":"j","K":"k","L":"l","M":"m","N":"n"
        #            ,"O":"o","P":"p","Q":"q","R":"r","S":"s","T":"t"
        #            ,"U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
        # result = ""
        # for s in str:
        #     if s in dictStr:
        #         result += dictStr[s]
        #     else:
        #         result += s
        #
        # # print(result)
        # return result

        # print("    Sloution3:")
        # print("        Runtime: 36 ms, faster than 55.73% of Python3 online submissions for To Lower Case.")
        # print("        Memory Usage: 13.2 MB, less than 5.45% of Python3 online submissions for To Lower Case.")
        result = ""
        for s in str:
            if s <= "Z" and s >= "A":
                # ord 转字符串为10进制数据 chr转10进制数据为字符串
                result += (chr)((ord)(s) + 32)
            else:
                result += s
        return result

    # 字符过滤
    def numUniqueEmails(self, emails:list) -> int:
        print("func numUniqueEmails")
        print("    Sloution1:")
        print("        Runtime: 48 ms, faster than 80.59% of Python3 online submissions for Unique Email Addresses.")
        print("        Memory Usage: 13.2 MB, less than 5.79% of Python3 online submissions for Unique Email Addresses.")

        result = set()
        for str in emails:
            name, domain = str.split("@")
            strTemp = name.split("+")[0]
            strFinal = strTemp.replace(".","")
            strFinal += "@" + domain
            result.add(strFinal)

        print(result)
        return len(result)

        pass

    # 字符识别
    def uniqueMorseRepresentations(self, words:list) -> int:
        print("func uniqueMorseRepresentations")
        print("    Sloution1:")
        print("        Runtime: 40 ms, faster than 57.57% of Python3 online submissions for Unique Morse Code Words.")
        print("        Memory Usage: 13.2 MB, less than 5.36% of Python3 online submissions for Unique Morse Code Words.")
        # 创建字典
        dictMorse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.",
                     "h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.",
                     "o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
                     "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}

        # 创建集合
        result = set()
        for strWord in words:
            strTemp = ""
            for char in strWord:
                strTemp += dictMorse[char]
            # print(strTemp)

            # 利用集合不会有重复元素的特性
            result.add(strTemp)

        return len(result)

    # 找到重复数据
    def repeatedNTimes(self, A:list) -> int:

        print("func repeatedNTimes")
        print("    Sloution1:")
        print("        Runtime: 48 ms, faster than 85.07% of Python3 online submissions for N-Repeated Element in Size 2N Array.")
        print("        Memory Usage: 14.1 MB, less than 5.12% of Python3 online submissions for N-Repeated Element in Size 2N Array.")
        dict = {}
        for char in A:
            if char in dict:
                print(char)
                return char
            else:
                dict[char] = 1


    # 奇偶排序
    def sortArrayByParity(self, A:list) -> list:
        print("func sortArrayByParity")
        # print("    Sloution1:")
        # print("        Runtime: 76 ms, faster than 54.04% of Python3 online submissions for Sort Array By Parity.")
        # print("        Memory Usage: 13.8 MB, less than 5.69% of Python3 online submissions for Sort Array By Parity.")
        # # 声明固定大小list
        # listTemp = list(range(len(A)))
        # evenSign = 0
        # oddSign  = -1
        #
        # # 遍历
        # for char in A:
        #     if (char % 2) == 0:
        #         listTemp[evenSign] = char
        #         evenSign += 1
        #     else:
        #         listTemp[oddSign] = char
        #         oddSign -= 1
        # print(listTemp)
        # return listTemp

        # print("    Sloution2:")
        #         # print("        Runtime: 72 ms, faster than 68.22% of Python3 online submissions for Sort Array By Parity.")
        #         # print("        Memory Usage: 13.7 MB, less than 5.69% of Python3 online submissions for Sort Array By Parity.")
        #         # # 声明固定大小list
        #         # oddSign  = len(A) - 1
        #         # listTemp = list(range(oddSign + 1))
        #         # evenSign = 0
        #         #
        #         # # 遍历
        #         # for char in A:
        #         #     if (char % 2) == 0:
        #         #         listTemp[evenSign] = char
        #         #         evenSign += 1
        #         #     else:
        #         #         listTemp[oddSign] = char
        #         #         oddSign -= 1
        #         # print(listTemp)
        #         # return listTemp
        #
        # print("    Sloution3:")
        # print("        Runtime: 100 ms, faster than 25.70% of Python3 online submissions for Sort Array By Parity.")
        # print("        Memory Usage: 13.8 MB, less than 5.69% of Python3 online submissions for Sort Array By Parity.")
        # # 声明固定大小list
        # listTemp = []
        #
        # # 遍历
        # for char in A:
        #     if (char % 2) == 0:
        #         listTemp.insert(0, char)
        #
        #     else:
        #         listTemp.append(char)
        #
        # print(listTemp)
        # return listTemp


        print("    Sloution4:")
        print("        Runtime: 72 ms, faster than 68.22% of Python3 online submissions for Sort Array By Parity.")
        print("        Memory Usage: 13.7 MB, less than 5.69% of Python3 online submissions for Sort Array By Parity.")
        # 声明空list
        listEven = []
        listOdd  = []
        # 遍历
        for char in A:
            if (char % 2) == 0:
                listEven.append(char)

            else:
                listOdd.append(char)

        print(listEven + listOdd)
        return listEven + listOdd

    # 数字乘法+排序
    def sortedSquares(self, A:list) -> list:
        print("func sortedSquares")
        # print("    Sloution1:")
        # print("        Runtime: 184 ms, faster than 32.21% of Python3 online submissions for Squares of a Sorted Array.")
        # print("        Memory Usage: 14.4 MB, less than 30.06% of Python3 online submissions for Squares of a Sorted Array.")
        # i = 0
        # for temp in A:
        #     A[i] = temp * temp
        #     i += 1
        # A.sort()
        # print (A)
        # return A


        print("    Sloution2:")
        print("        Runtime: 164 ms, faster than 60.46% of Python3 online submissions for Squares of a Sorted Array.")
        print("        Memory Usage: 15.2 MB, less than 5.22% of Python3 online submissions for Squares of a Sorted Array.")
        listTemp = []
        for temp in A:
            listTemp.append(temp * temp)
        listTemp.sort()
        print (listTemp)
        return listTemp

    # 多维数组变换排序 重点在于 1 如何声明多维数组 2 多维数组不能直接append
    def flipAndInvertImage(self, A):

        # print("func flipAndInvertImage")
        # print("    Sloution1:")
        # print("        Runtime: 52 ms, faster than 48.58% of Python3 online submissions for Flipping an Image.")
        # print("        Memory Usage: 13.3 MB, less than 5.63% of Python3 online submissions for Flipping an Image.")
        # # result = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        # result = [[] for j in range(len(A))]
        # j = 0
        # for listFirst in A:
        #     i = -1
        #     # print(listFirst)
        #     for listFinal in listFirst:
        #         # result[j][i] = 1 - listFinal
        #         result[j].append(1 - listFirst[i])
        #         # print("listTemp[i]", listTemp[i], listFinal, i)
        #         i -= 1
        #     j += 1
        #     print("result after: ", result)
        # print(result)
        # return result

        # print("    Sloution2:")
        # print("        Runtime: 68 ms, faster than 22.15% of Python3 online submissions for Flipping an Image.")
        # print("        Memory Usage: 13.3 MB, less than 5.63% of Python3 online submissions for Flipping an Image.")
        # result = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        # j = 0
        # for listFirst in A:
        #     i = -1
        #     # print(listFirst)
        #     for listFinal in listFirst:
        #         result[j][i] = 1 - listFinal
        #         i -= 1
        #     j += 1
        # print(result)
        # return result

        # 方法3主要用到reverse list内部反向排序  map 函数序列映射 以及 lambda功能
        print("    Sloution3:")
        print("        Runtime: 52 ms, faster than 48.58% of Python3 online submissions for Flipping an Image.")
        print("        Memory Usage: 13.2 MB, less than 5.63% of Python3 online submissions for Flipping an Image.")
        for i in range(len(A)):
            # list组内元素交换
            A[i].reverse()
            A[i] = (list)(map(lambda x:1-x, A[i]))

        print(A)
        return A

        pass


    def numRookCaptures(self, board) -> int:

        print("func numRookCaptures")
        print("    Sloution1:")
        print("        Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Available Captures for Rook.")
        print("        Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Available Captures for Rook.")
        # result = [[0 for i in range(len(A[0]))] for j in range(len(A))]

        MAX_SIZE = 8
        # 遍历得到"R"
        for y in range(MAX_SIZE):
            for x in range(MAX_SIZE):
                if board[y][x] == "R":
                    row  = y
                    rank = x
                    # print("rank = ", rank, "row = ", row)

        # 处理横轴
        strRow = "." + ("".join(board[row])).replace(".", "") + "."
        # print("listRow:", strRow, board[row])
        count = 0
        # 遍历找到R
        for i in range(len(strRow)):
            if strRow[i] == "R":
                if strRow[i]+strRow[i - 1] == "Rp":
                    count += 1
                if strRow[i]+strRow[i + 1] == "Rp":
                    count += 1
                break

        # 处理纵轴
        # 遍历找到R
        temp = 0
        strRank = "."
        for i in range(MAX_SIZE):
            # print("board[i][rank]", board[i][rank])
            if (board[i][rank] == "B") or (board[i][rank] == "p"):
                strRank += board[i][rank]
                temp += 1
            if board[i][rank] == "R":
                strRank += board[i][rank]
                temp += 1
                location = temp
        strRank += "."
        # print("strRank", strRank, location)
        if strRank[location] + strRank[location - 1] == "Rp":
            count += 1
        if strRank[location] + strRank[location + 1] == "Rp":
            count += 1
        print("count:", count)
        return count

    def diStringMatch(self, S: str) -> list:
        print("func DI String Match")
        print("    Sloution1:")
        print("        Runtime: 92 ms, faster than 62.95% of Python3 online submissions for DI String Match.")
        print("        Memory Usage: 14.2 MB, less than 5.62% of Python3 online submissions for DI String Match.")
        iIncrease = 0
        dDecrease = len(S)
        listReturn = []
        for s in S:
            if s == "I":
                listReturn.append(iIncrease)
                iIncrease += 1
            else:
                listReturn.append(dDecrease)
                dDecrease -= 1

        listReturn.append(iIncrease)
        print(listReturn)
        return listReturn

    def maximum69Number(self, num: int) -> int:
        maxNum = num
        numStr = str(num)
        for i in range(len(numStr)):
            if numStr[i] == '6':
                maxNum += 3 * pow( 10, len(numStr) - i - 1)
                break
        # print(maxNum)
        return maxNum

    def replaceElements(self, arr: List[int]) -> List[int]:
        outList = [-1]

        # 倒序遍历
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > outList[-1]:
                outList.append(arr[i])
            else:
                outList.append(outList[-1])

        outList.reverse()
        return outList

    def run(self):

        startTime = time.time()
        # self.numJewelsInStones("aA", "aAAbbbb")
        # self.toLowerCase(testStr)
        # self.numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"])
        # self.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
        # self.repeatedNTimes([5,1,5,2,5,3,5,4])
        # self.sortArrayByParity([3,1,2,4])
        # self.sortedSquares([-4,-1,0,3,10])
        # self.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
        # self.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])
        # self.diStringMatch("IDID")
        # self.maximum69Number(9669)
        self.replaceElements([17,18,5,4,6,1])
        endTime = time.time()
        print("run time: ", (str(endTime - startTime))[:8], "s")

        pass

