#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 消息回声脚本

import sys


def echo():
    """
    消息回声，无论怎样的请求都使用print输出

    :return: None
    """
    if len(sys.argv) < 2:
        print 'Usage: {} msg'.format(__file__)
        sys.exit(1)
    msg = sys.argv[1]
    print msg


if __name__ == '__main__':
    echo()
