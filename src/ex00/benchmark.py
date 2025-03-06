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

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
              'anna@live.com', 'philipp@gmail.com'] * 5
    time_cycle = timeit.timeit(lambda: cycle_func(emails), number=90_000_000)
    time_list_comp = timeit.timeit(lambda: list_comp_func(emails), number=90_000_000)
    print(('it is better to use a loop', 
           'it is better to use a list comprehension')[time_list_comp <= time_cycle])
    time1, time2 = sorted([time_cycle, time_list_comp])
    print(f'{time1} vs {time2}')
    # print(cycle_func(emails), list_comp_func(emails), sep='\n')

if __name__ == '__main__':
    main()
