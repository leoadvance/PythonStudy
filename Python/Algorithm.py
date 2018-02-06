#coding=utf-8
import time
from ListNode import ListNode
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
                # print("l1.val =", l1.val)
                l1 = l1.next

            if (l2):
                carry += l2.val
                # print("l2.val =", l2.val)
                l2 = l2.next

            nextList.next = ListNode(carry % 10)
            nextList = nextList.next
            carry //= 10

        return listOut.next



    def twoSumTest(self):

        print ("")
        list1 = [10002,10004,10006,10008,10010,10012,10014,10016,10018,10020,10022,10024,10026,10028,10030,10032,10034,10036,10038,10040,10042,10044,10046,10048,10050,10052,10054,10056,10058,10060,10062,10064,10066,10068,10070,10072,10074,10076,10078,10080,10082,10084,10086,10088,10090,10092,10094,10096,10098,10100,10102,10104,10106,10108,10110,10112,10114,10116,10118,10120,10122,10124,10126,10128,10130,10132,10134,10136,10138,10140,10142,10144,10146,10148,10150,10152,10154,10156,10158,10160,10162,10164,10166,10168,10170,10172,10174,10176,10178,10180,10182,10184,10186,10188,10190,10192,10194,10196,10198,10200,10202,10204,10206,10208,10210,10212,10214,10216,10218,10220,10222,10224,10226,10228,10230,10232,10234,10236,10238,10240,10242,10244,10246,10248,10250,10252,10254,10256,10258,10260,10262,10264,10266,10268,10270,10272,10274,10276,10278,10280,10282,10284,10286,10288,10290,10292,10294,10296,10298,10300,10302,10304,10306,10308,10310,10312,10314,10316,10318,10320,10322,10324,10326,10328,10330,10332,10334,10336,10338,10340,10342,10344,10346,10348,10350,10352,10354,10356,10358,10360,10362,10364,10366,10368,10370,10372,10374,10376,10378,10380,10382,10384,10386,10388,10390,10392,10394,10396,10398,10400,10402,10404,10406,10408,10410,10412,10414,10416,10418,10420,10422,10424,10426,10428,10430,10432,10434,10436,10438,10440,10442,10444,10446,10448,10450,10452,10454,10456,10458,10460,10462,10464,10466,10468,10470,10472,10474,10476,10478,10480,10482,10484,10486,10488,10490,10492,10494,10496,10498,10500,10502,10504,10506,10508,10510,10512,10514,10516,10518,10520,10522,10524,10526,10528,10530,10532,10534,10536,10538,10540,10542,10544,10546,10548,10550,10552,10554,10556,10558,10560,10562,10564,10566,10568,10570,10572,10574,10576,10578,10580,10582,10584,10586,10588,10590,10592,10594,10596,10598,10600,10602,10604,10606,10608,10610,10612,10614,10616,10618,10620,10622,10624,10626,10628,10630,10632,10634,10636,10638,10640,10642,10644,10646,10648,10650,10652,10654,10656,10658,10660,10662,10664,16020,1]

        self.twoSum(list1, 16021)
        return

    def __init__(self):

        print("初始化Algorithm类")

        self.twoSumTest()
        self.reverse(100)

        self.isPalindrome(-2147483648)
        self.romanToInt("XXDCI")
        a = ListNode(2)
        a.next = a1 = ListNode(4)
        a1.next = ListNode(3)
        b = ListNode(5)
        b.next = b1 = ListNode(6)
        b1.next = b2 = ListNode(4)

        self.addTwoNumbers(a, b)
        return
