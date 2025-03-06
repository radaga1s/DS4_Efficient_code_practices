#!/usr/bin/env python3

import timeit

def cycle_func(emails: list) -> list:
    res = []
    for email in emails:
        if email.endswith('@gmail.com'):
            res.append(email)
    return res

def list_comp_func(emails: list) -> list:
    return [email for email in emails if email.endswith('@gmail.com')]

def map_func(emails: list):
    return map(lambda x: x if x.endswith('@gmail.com') else None, emails)

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
              'anna@live.com', 'philipp@gmail.com'] * 5
    time_cycle = (timeit.timeit(lambda: cycle_func(emails), number=90_000_000), 'loop')
    time_list_comp = (timeit.timeit(lambda: list_comp_func(emails), number=90_000_000), 'list comprehension') 
    time_map = (timeit.timeit(lambda: map_func(emails), number=90_000_000), 'map')
    time1, time2, time3 = sorted([time_cycle, time_list_comp, time_map], key=lambda x: x[0])
    print(f'it is better to use a {time1[1]}')
    print(f'{time1[0]} vs {time2[0]} vs {time3[0]}')
    # print(cycle_func(emails), list_comp_func(emails), list(map_func(emails)), sep='\n')

if __name__ == '__main__':
    main()
