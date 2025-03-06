#!/usr/bin/env python3

import timeit
import sys

def cycle_func(emails: list) -> list:
    res = []
    for email in emails:
        if email.endswith('@gmail.com'):
            res.append(email)
    return res

def list_comp_func(emails: list) -> list:
    return [email for email in emails if email.endswith('@gmail.com')]

def map_func(emails: list):
    return [i for i in map(lambda x: x if x.endswith('@gmail.com') else None, emails) if i]

def filter_func(emails: list):
    return list(filter(lambda x: x.endswith('@gmail.com'), emails))

def raise_exc(_):
    raise Exception("Wrong funcion's name")

def main():
    if len(sys.argv) != 3: return
    f_name, amount = sys.argv[1], int(sys.argv[2])
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
              'anna@live.com', 'philipp@gmail.com'] * 5
    d = dict(loop=cycle_func, list_comprehension=list_comp_func, map=map_func, filter=filter_func)
    func = d.get(f_name, raise_exc)
    print(timeit.timeit(lambda: func(emails), number=amount))
    # print(func(emails))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
