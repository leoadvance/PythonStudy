# couding=utf-8
import re
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
        # print("        Runtime: 40 ms, faster than 34.23% of Python3 online submissions for To Lower Case.")
        # print("        Memory Usage: 13.4 MB, less than 5.45% of Python3 online submissions for To Lower Case.")
        # dictStr = {"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g"
        #            ,"H":"h","I":"i","J":"j","K":"k","L":"l","M":"m","N":"n"
        #            ,"O":"o","P":"p","Q":"q","R":"r","S":"s","T":"t"
        #            ,"U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
        # liststr = list(str)
        # for i in range(len(liststr)):
        #     if liststr[i] in dictStr:
        #         liststr[i] = dictStr[liststr[i]]
        #
        # print(liststr)
        # return "".join(liststr)
        print("    Sloution3:")
        print("        Runtime: 36 ms, faster than 55.73% of Python3 online submissions for To Lower Case.")
        print("        Memory Usage: 13.2 MB, less than 5.45% of Python3 online submissions for To Lower Case.")
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
        print("        Runtime: 60 ms, faster than 41.33% of Python3 online submissions for Unique Email Addresses.")
        print("        Memory Usage: 13.3 MB, less than 5.79% of Python3 online submissions for Unique Email Addresses.")

        dictTemp = {}
        for str in emails:
            name, domain = str.split("@")
            strTemp = name.split("+")[0]
            strFinal = strTemp.replace(".","")
            strFinal += "@" + domain
            if strFinal not in dictTemp:
                dictTemp[strFinal] = 1

        print(dictTemp)
        return len(dictTemp)

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

    def run(self):
        # self.numJewelsInStones("aA", "aAAbbbb")
        # self.toLowerCase("ABYebcd")
        # self.numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"])
        self.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
        pass