# -*- coding:utf-8 -*-
#第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）

import random
import string

sampleString = string.ascii_letters+'0123456789#$%&()'
#print('sampleString:',sampleString)

def generateCode(codeCount, codeLen):

    for code in range(codeCount):
        results=''.join(random.sample(sampleString,codeLen))
        print(results)

codeLen = int(input('please input your code length:'))
codeCount = int(input('please input your code count:'))

generateCode(codeCount, codeLen)