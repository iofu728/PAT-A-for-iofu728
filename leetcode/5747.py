# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-05-02 12:06:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-05-02 12:06:31

"""
5747. 将字符串拆分为递减的连续值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个仅由数字组成的字符串 s 。

请你判断能否将 s 拆分成两个或者多个 非空子字符串 ，使子字符串的 数值 按 降序 排列，且每两个 相邻子字符串 的数值之 差 等于 1 。

例如，字符串 s = "0090089" 可以拆分成 ["0090", "089"] ，数值为 [90,89] 。这些数值满足按降序排列，且相邻值相差 1 ，这种拆分方法可行。
另一个例子中，字符串 s = "001" 可以拆分成 ["0", "01"]、["00", "1"] 或 ["0", "0", "1"] 。然而，所有这些拆分方法都不可行，因为对应数值分别是 [0,1]、[0,1] 和 [0,0,1] ，都不满足按降序排列的要求。
如果可以按要求拆分 s ，返回 true ；否则，返回 false 。

子字符串 是字符串中的一个连续字符序列。

 

示例 1：

输入：s = "1234"
输出：false
解释：不存在拆分 s 的可行方法。
示例 2：

输入：s = "050043"
输出：true
解释：s 可以拆分为 ["05", "004", "3"] ，对应数值为 [5,4,3] 。
满足按降序排列，且相邻值相差 1 。
示例 3：

输入：s = "9080701"
输出：false
解释：不存在拆分 s 的可行方法。
示例 4：

输入：s = "10009998"
输出：true
解释：s 可以拆分为 ["100", "099", "98"] ，对应数值为 [100,99,98] 。
满足按降序排列，且相邻值相差 1 。
 

提示：

1 <= s.length <= 20
s 仅由数字组成
"""


class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(before, s):

            if before != None and before - 1 == int(s):
                self.flag = True
                return
            if self.flag or (before and before - 1 > int(s)) or not s:
                return
            if before == None:
                n = len(s)
                idx, b = 1, int(s[0])
                dfs(int(s[:idx]), s[idx:])
                while idx < n:
                    if int(s[:idx]) != b:
                        dfs(int(s[:idx]), s[idx:])
                        b = int(s[:idx])
                    idx += 1
            else:
                n = len(s)
                idx, b = 1, int(s[0])
                if b == before - 1:
                    dfs(int(s[:idx]), s[idx:])
                while idx < n:
                    if int(s[:idx]) != b and int(s[:idx]) == before - 1:
                        dfs(int(s[:idx]), s[idx:])
                        b = int(s[:idx])
                    idx += 1

        N = len(s)
        if N <= 1:
            return False
        self.flag = False
        dfs(None, s)
        return self.flag
