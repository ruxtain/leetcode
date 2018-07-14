#! /Users/michael/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Author: Michael Tan
# @Date:   2018-07-14 15:16:48
# @Last Modified by:   Michael Tan
# @Last Modified time: 2018-07-14 15:23:41

'''
https://leetcode-cn.com/problems/self-dividing-numbers/description/

自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：

输入： 
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
注意：

每个输入参数的边界满足 1 <= left <= right <= 10000。
'''

def fun(left, right):
    '''
    很简单，不解释。
    '''
    results = []
    for i in range(left, right + 1):
        n = str(i)
        if '0' not in n:
            if all([i % int(j) == 0 for j in n]):
                results.append(i)
    return results

print(fun(1, 22))
print(fun(1, 10000))

