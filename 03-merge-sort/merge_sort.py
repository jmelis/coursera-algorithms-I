#!/usr/bin/env python2

import sys

def merge(a,b):
    size = len(a) + len(b)
    c = []

    i = j = 0
    while len(c) < size:
        if a[i] < b[j]:
            c.append(a[i])

            if i<len(a)-1:
                i+=1
            else:
                c.extend(b[j:])
        else:
            c.append(b[j])

            if j<len(b)-1:
                j+=1
            else:
                c.extend(a[i:])

    return c

def merge_sort(l):
    if len(l) == 1:
        return l

    h = len(l)/2

    a = merge_sort(l[:h])
    b = merge_sort(l[h:])

    return merge(a,b)

if __name__ == '__main__':
    l = [int(i) for i in sys.argv[1:]]
    sl = merge_sort(l)
    print sl
    print sl == sorted(l)
