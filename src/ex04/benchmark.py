#!/usr/bin/env python3

import timeit
from random import randint
from collections import Counter as cnt

def get_dict(lst: list) -> dict:
    d = {}
    for k in lst:
        d[k] = d.get(k, 0) + 1
    return d

def get_most(lst: list) -> dict:
    d = get_dict(lst)
    return {k: d[k] for k in sorted(d, key=d.get, reverse=True)[:10]}

def get_dict_cnt(lst: list):
    return cnt(lst)

def get_most_cnt(lst: list):
    return cnt(lst).most_common(10)

def main():
    vals = [randint(0, 100) for _ in range(1_000_000)]
    for s, func in (('my function:', get_dict), ('Counter:', get_dict_cnt),
                     ('my top:', get_most), ("Counter's top:", get_most_cnt)):
        print(f'{s} {timeit.timeit(lambda: func(vals), number=1):.7f}')
    # print(get_most(vals))
    # print(dict(get_most_cnt(vals)))


if __name__ == '__main__':
    main()
