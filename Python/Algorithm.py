#coding=utf-8
import time
from ListNode import ListNode
from ListNode import TreeNode
class Algorithm:


    def twoSum(self, nums, target):
        listReturn = [99, 99]
        start =time.time()
        listLen = len(nums)


        # for i in range(0, listLen - 1):
        #     for j in range (i + 1, listLen):
        #
        #         if (nums[i] + nums[j] == target):
        #
        #             listReturn[0] = i
        #             listReturn[1] = j
        #             print (i, j)
        #             stop = time.time()
        #             print("函数运行时间：",stop-start)
        #             return listReturn
        # 声明空字典
        mydict = {}

        # 遍历
        for i in range(0, listLen):

            # 判断该值是否在字典中出现过
            if nums[i] in mydict:
                stop = time.time()
                print("函数运行时间：", stop - start, "s")
                print (mydict[nums[i]], i, nums[mydict[nums[i]]], nums[i])
                return [mydict[nums[i]], i]

            else:

                # 记录需要获取的相反数 用序号做值
                mydict[target-nums[i]] = i

    def reverse(self, x):
        print("数据逆序&取反,超过32位有符号int算溢出，溢出输出0,原数值 =", x)
        output = 0
        sign   = 0

        if x < 0 :
            x = 0 - x
            sign = 1
        while(x > 0):
            output *= 10
            output += x % 10
            x //= 10
        if sign == 1:
            output = 0 - output

        if output < -2147483648 or output > 2147483647:
            output = 0
        print ("逆序值 =", output)
        return output

    # 判断是否回文数字
    def isPalindrome(self, x):
        print("判断是否回文数字！x = ", x)
        out = 0
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        while (out <= x):
            out *= 10
            out += x % 10
            x //= 10
            if (out == x):
                # print("是回文")
                return True
            elif (x > 9) and (out == x // 10):
                return True

        # print("不是回文")
        return False

    # roman数字转整型
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        print("1~3999roman数字转整型，原始值 s = ", s)
        # 初始化字典
        r_sum = 0
        temp = 0
        rul = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for ch in s:
            ch_val = int(rul[ch])
            r_sum = r_sum + ch_val
            if temp < ch_val:
                r_sum -= temp * 2
            temp = ch_val
        print("r_sum =", r_sum)
        return r_sum

    # 链表求和
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print("两链表求和")

        # 声明链表
        listOut = nextList = ListNode(0)
        carry = 0

        # 判断链表和进位位非空
        while (l1 or l2 or carry):
            if (l1):
                carry += l1.val
                #print("l1.val =", l1.val)
                l1 = l1.next

            if (l2):
                carry += l2.val
                #print("l2.val =", l2.val)
                l2 = l2.next

            nextList.next = ListNode(carry % 10)
            nextList = nextList.next
            carry //= 10

        return listOut.next

    # 最长数值
    def isInListNode(self, l1, s):
        if l1.val == s:
            return


    # 最长数值
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print("求连续不同字符长度 ", s)


        if (len(s) == 0):
            return 0
        maxLen = returnLen = 1

        # 记录首个链表
        listHead = listReal = ListNode(s[0])


        for str in s[1:]:
            # 遍历列表
            lenSize = 0
            sign = 0


            # print("Current list = ")
            # listTemp = listHead
            # while(listTemp):
            #     print(listTemp.val)
            #     listTemp = listTemp.next


            # 判断当前链表中是否有相同数据
            listTemp = listHead
            while(listTemp):
               # print("链表当前值", listTemp.val, "待对比值", str)
                # 有相同值
                if (listTemp.val == str):
                    sign = 1
                    # 非最后一位（即非连续）
                    if (listTemp.next != None):
                        listHead = listTemp.next
                        returnLen -= lenSize
                        listReal.next = ListNode(str)
                        listReal = listReal.next
                        break
                    # 最后一位 长度归0
                    else:
                        listHead = listReal = ListNode(str)
                        #print("listHead.val =", listHead.val)
                        returnLen = 1
                        break
                # 未找到相同值
                else:
                    lenSize += 1
                    listTemp = listTemp.next
            # 未找下相同数据 记录新长度
            if (sign == 0):

                listReal.next = ListNode(str)
                listReal = listReal.next
                returnLen += 1
                #print("未找到相同数，追加值 = ", str, "长度 =", returnLen)
            if (returnLen > maxLen):
                maxLen = returnLen
               # print("当前最大长度 =", maxLen)
        print("不同数据长度 =", maxLen)


        return maxLen

    def twoSumTest(self):

        print ("")
        list1 = [10002,10004,10006,10008,10010,10012,10014,10016,10018,10020,10022,10024,10026,10028,10030,10032,10034,10036,10038,10040,10042,10044,10046,10048,10050,10052,10054,10056,10058,10060,10062,10064,10066,10068,10070,10072,10074,10076,10078,10080,10082,10084,10086,10088,10090,10092,10094,10096,10098,10100,10102,10104,10106,10108,10110,10112,10114,10116,10118,10120,10122,10124,10126,10128,10130,10132,10134,10136,10138,10140,10142,10144,10146,10148,10150,10152,10154,10156,10158,10160,10162,10164,10166,10168,10170,10172,10174,10176,10178,10180,10182,10184,10186,10188,10190,10192,10194,10196,10198,10200,10202,10204,10206,10208,10210,10212,10214,10216,10218,10220,10222,10224,10226,10228,10230,10232,10234,10236,10238,10240,10242,10244,10246,10248,10250,10252,10254,10256,10258,10260,10262,10264,10266,10268,10270,10272,10274,10276,10278,10280,10282,10284,10286,10288,10290,10292,10294,10296,10298,10300,10302,10304,10306,10308,10310,10312,10314,10316,10318,10320,10322,10324,10326,10328,10330,10332,10334,10336,10338,10340,10342,10344,10346,10348,10350,10352,10354,10356,10358,10360,10362,10364,10366,10368,10370,10372,10374,10376,10378,10380,10382,10384,10386,10388,10390,10392,10394,10396,10398,10400,10402,10404,10406,10408,10410,10412,10414,10416,10418,10420,10422,10424,10426,10428,10430,10432,10434,10436,10438,10440,10442,10444,10446,10448,10450,10452,10454,10456,10458,10460,10462,10464,10466,10468,10470,10472,10474,10476,10478,10480,10482,10484,10486,10488,10490,10492,10494,10496,10498,10500,10502,10504,10506,10508,10510,10512,10514,10516,10518,10520,10522,10524,10526,10528,10530,10532,10534,10536,10538,10540,10542,10544,10546,10548,10550,10552,10554,10556,10558,10560,10562,10564,10566,10568,10570,10572,10574,10576,10578,10580,10582,10584,10586,10588,10590,10592,10594,10596,10598,10600,10602,10604,10606,10608,10610,10612,10614,10616,10618,10620,10622,10624,10626,10628,10630,10632,10634,10636,10638,10640,10642,10644,10646,10648,10650,10652,10654,10656,10658,10660,10662,10664,16020,1]

        self.twoSum(list1, 16021)
        return

    # 字符排序
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        print("字符排序")
        if numRows == 1:
            return s


        period = 2 * (numRows - 1)

        # 声明list缓存
        lines = ["" for i in range(numRows)]

        # 字典保存余数
        d = {}

        # 下标余数对应到行
        for i in range(period):
            if i < numRows:
                d[i] = i
            else:
                d[i] = period - i

        for i in range(len(s)):
            lines[d[i % period]] += s[i]

        print(lines)

        # list变字符串
        print("".join(lines))
        return "".join(lines)

    # 计算汉明长度
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        print("计算汉明长度")

        # 先异或 相同为0 不同为1
        c  = x^y
        len = 0

        # 统计异或值1的个数
        while(c):
            if (c % 2):
                len += 1
            c >>= 1
        print (len)
        return len


    # 原点判断
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        print("原点回归")
        dict = {"U":0, "D":1, "L":2, "R":3 }
        list = [0] * 4
        for s in moves:
            list[dict[s]] +=1
        if (list[0] == list[1]) and (list[2] == list[3]):
            return True

        return False

    # 自除数
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        list = []
        # print("自除数 list长度 = ", len(list))
        i = left
        Sign = 0
        while (i <= right):
            num = i
            #print ("i=", i)
            if (num > 9):
                while (num):
                    remainder = num % 10
                    # 余数不能为0
                    if (remainder == 0):
                        i += 1
                        Sign = 1
                        break
                    if ((i % remainder) == 0):
                        num //= 10
                    else:
                        i += 1
                        Sign = 1
                        break
            if (Sign == 0):
                list.append(i)
                i += 1
            else:
                Sign = 0
        print(list)
        return list

    def printer_error(self, s):
        # your code
        badLen = 0
        totalLen = len(s)
        for strS in s:
            if strS > "m":
                badLen += 1

        return (str(badLen) + "/" + str(totalLen))

    def square_digits(self, num):
        # my solutions
        # returnNum = 0
        # listNum = []
        #
        # while(num):
        #     num, remainder = divmod(num, 10)
        #     listNum.append(remainder * remainder)
        #
        # for intnum in listNum[::-1]:
        #     if intnum > 10:
        #         returnNum *= 100
        #     else:
        #         returnNum *= 10
        #     returnNum += intnum
        #
        # print(listNum, returnNum)
        # return (returnNum)

        # best solutions
        ret = ""
        for x in str(num):
            ret += (str(int(x)**2))
        print(ret)

    def get_sum(self, a, b):
        print("求ab之和")

        # 变量交换，保证a<=b
        if (a > b):
             a,b = b,a

        sum = 0
        i   = a

        while(i <= b):
            sum += i
            i += 1
        print(sum)
        return sum

    def tribonacci(self, signature, n):

        print("费波那契数列")
        listOut = signature[:]
        sum = listOut[0] + listOut[1]
        i = 3
        if n > 3:
            while(i < n):
                sum += listOut[i - 1]
                listOut.append(sum)
                sum -=listOut[i - 3]
                i += 1
        print(listOut[:n])

    def find_missing_letter(self, chars):

        for i in range(len(chars) - 1):

            # ord 字符串转ASCII chr ascii 转字符串
            if (ord(chars[i + 1]) - ord(chars[i]) != 1):
                print(chr(ord(chars[i]) + 1))



    def sumDigits(self, number):

        print("求数值各位之和")
        number = abs(number)

        sum = 0
        while(number):
            number, remainder = divmod(number, 10)
            sum += remainder

        print(sum)

    def disemvowel(self, string):
        dict = {"a","e","i","o","u","A","E","I","O","U"}
        sOut = ""
        for x in string:
            if (x in dict) is False:
                sOut += x
        #print(sOut)
        return sOut

    # 字符倒序
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strOut = ""
        for x in s.split(" "):
            strOut += x[:: -1]
            strOut += " "
        print(strOut[:-1])

    # 排序+求最小值
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 降序排列
        a = sorted(nums, reverse=False)
        print(a)
        # for i in a:
        #     print (sum(a[::2]))
        # print(sum(sorted(nums)[::3]))
        print(sum(a[::3]))

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        print(matrix)
        print(matrix[2][1])

        line = len(matrix)
        row  = len(matrix[0])
        print("数组 = ",row, "x", line)
        n = 0
        while (n < line - 1):
            for i in range (row - 1):
                print("n =", n, "i = ", i)
                if (matrix[n][i] != matrix[n+1][i+1]):
                    return False

            n += 1
        return True

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print("判断数组里唯一出现一次的数")
        # lenSize = len(nums)
        # if lenSize == 1:
        #     return nums[0]
        #
        # # 按升序排列
        # listout = sorted(nums)
        # print(listout)
        #
        # i = 0
        # while (i < lenSize - 1):
        #     if (listout[i] != listout[i + 1]):
        #         print(listout[i])
        #         return listout[i]
        #     i += 2
        # print(listout[i])
        # return listout[i]
        # 声明字典
        dict = {}

        for i in nums:
            # 移除指定数，如该数不存在，则写入字典
            try:
                dict.pop(i)
            except:
                dict[i] = 1
            print ("dict = ", dict)

        # 返回内容首位
        return(dict.popitem()[0])

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # 分糖果本质是求一堆数里面最大不同数据个数（不超过总数一半），所以采用字典方式求解
        print("分糖果")
        # dict = {}
        # lenMAX = len(candies) >> 1
        # lenCurrent = 0
        # for i in candies:
        #     print(i)
        #     if (i in dict) is False:
        #         dict[i] = 1000000
        #         lenCurrent += 1
        #         if (lenCurrent == lenMAX):
        #             break
        #
        # print(dict)
        # print("lenCurrent = ",lenCurrent)


        # 网络解法
        print("candies", candies)
        lenMax = len(candies) >> 1
        candies = set(candies)
        lenCurrent = len(candies)
        print(candies)
        if lenCurrent > lenMax:
            return lenCurrent
        else:
            return lenMax

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 我的解法
        # lenTotal = len(nums)
        # print("lenTotal =", lenTotal)
        # if lenTotal < 2:
        #     return nums
        # lastSign = lenTotal - 1
        #
        # i = lastSign
        # while(i >= 0):
        #     if nums[i] == 0:
        #         j = i
        #         while(j < lastSign):
        #             # 相邻交换
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             j += 1
        #     i -= 1
        # print(nums)

        # 官方解法1
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        # print(nums)

        # 官方解法2
        last0 = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                print("i = ", i, "nums[i] = ", nums[i], "nums[last0] = ",
                      nums[last0], "last0 =", last0)
                nums[i], nums[last0] = nums[last0], nums[i]
                last0 += 1
            print(nums)

    def letterCasePermutation(self, S):

        print("把字符串中所有字母变换大小写输出")

        # 声明列表组
        ans = [[]]

        # 遍历字符串
        for char in S:
             # 获取当前list组数
            n = len(ans)
            print("n =",n)

            # 如果该字符是字母
            if char.isalpha():

                # 遍历已有组数
                for i in range(n):
                    #复制内容 并分别增加大小写
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n + i].append(char.upper())
                    # print("ans =", ans)
            else:
                # 如果非字母，则仅添加
                for i in range(n):
                    ans[i].append(char)
                    # print("ans =", ans)
        # 列表内多个单字符串合并
        ans = list(map("".join, ans))
        return (ans)

    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
            print("target =", target)
        if target % 2 == 0:
            print (k)
        else :
            print(k + 1 + k % 2)

    def __init__(self):

        print("初始化Algorithm类")

        # self.twoSumTest()
        # self.reverse(100)
        #
        # self.isPalindrome(-2147483648)
        # self.romanToInt("XXDCI")
        # a = ListNode(2)
        # a.next = a1 = ListNode(4)
        # a1.next = ListNode(3)
        # b = ListNode(5)
        # b.next = b1 = ListNode(6)
        # b1.next=ListNode(4)
        #
        # self.addTwoNumbers(a, b)
        # self.lengthOfLongestSubstring("cckilbkkd")
        # self.convert("PAYPALISHIRING", 4)
        #
        # self.hammingDistance(1, 4)
        # self.judgeCircle("LLLL")
        # self.selfDividingNumbers(1, 22)
        # self.printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
        # self.square_digits(9129)
        # self.get_sum(3,3)
        # self.tribonacci([0.5,0.5,0.5], 10)
        # self.find_missing_letter(['O','Q','R','S'])
        # self.sumDigits(-32)
        # self.disemvowel("This website is for losers LOL!")
        # self.reverseWords("Let's take LeetCode contest")
        # self.arrayPairSum([5,7,6,3,4,1,2,8])
        # self.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
        # self.singleNumber([2,3,1,5,1,3,2])
        # self.distributeCandies([1,1,2,3])
        # self.moveZeroes([5,6,0,1,0,3,12])
        self.letterCasePermutation("a1b2")
        self.reachNumber(100)
        return
