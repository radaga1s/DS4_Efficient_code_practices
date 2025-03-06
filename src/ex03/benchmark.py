#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def loop_func(num):
    sm = 0
    for i in range(1, num+1):
        sm += i*i
    return sm

def reduce_func(num):
    return reduce(lambda x, y: x+y*y, range(1, num+1))

def raise_exc(_):
    raise Exception("Wrong funcion's name")

def main():
    if len(sys.argv) != 4: return
    f_name, amount, num = [int(i) if i.isdigit() else i for i in sys.argv[1:]]
    d = dict(loop=loop_func, reduce=reduce_func)
    func = d.get(f_name, raise_exc)
    print(timeit.timeit(lambda: func(num), number=amount))
    # print(func(num))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
