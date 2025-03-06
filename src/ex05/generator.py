#!/usr/bin/env python3

import sys
import resource

def get_list_from_csv(file_obj):
    while (line := file_obj.readline()):
        yield line

def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf8') as file:
        lines = get_list_from_csv(file)
        for _ in lines:
            pass
    ress = resource.getrusage(resource.RUSAGE_SELF)
    peak = ress.ru_maxrss / 1024**3
    time = ress.ru_utime + ress.ru_stime
    print(f'Peak Memory Usage = {peak:.3f} GB')
    print(f'User Mode Time + System Mode Time = {time:.2f}s')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
