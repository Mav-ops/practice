#!/usr/bin/env python

def safe_float(obj):
    'save version of float()'
    try:
        retval=float(obj)
    except (ValueError,TypeError) as diag:
        retval=str(diag)
    return retval

def main():
    'handeles all the data processing'
    log=open('carddata.txt','a')
    try:
        ccfile=open('carddata.txt','r')
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return

    txns=ccfile.readlines()
    ccfile.close()
    total=0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result=safe_float(eachTxn)
        if isinstance(result,float):
            total+=result
            log.write('data...processed\n')
        else:
            log.write('ignored:%s\n' % result)
    print('$%.2f (new balance)' % total)
    log.close()

if __name__=='__main__':
    main()