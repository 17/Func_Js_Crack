# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 11:56
# @Author  : Esbiya
# @Email   : 18829040039@163.com
# @File    : test.py
# @Software: PyCharm

import time
from yunpian.geetest import crack


def main():
    print('开始测试...')
    print('=' * 100)
    num = 1
    success = 0
    while num <= 20:
        x = crack()
        print(x)
        if x['success']:
            success += 1
        time.sleep(1)
        num += 1
    print('最后测试结果 >> %.2f%%' % success)


if __name__ == '__main__':
    main()
