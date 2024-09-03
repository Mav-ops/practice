# -*- coding: utf-8 -*-
import time
def testit(func,*arg):
    t0 = time.perf_counter()
    re = func(*arg)
    t1 = time.perf_counter()-t0
    return re,t1

if __name__ == '__main__':
    funcs = (int,float)
    vals = ('123',123)

    for eachfunc in funcs:
        print ('__________')
        for eachval in vals:
            retval = testit(eachfunc,eachval)
            print ('result: ',retval[0])
            print ('time:',retval[1])
