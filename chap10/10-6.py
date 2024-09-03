def try_open(filename,mode='r'):
    try:
        f=open(filename,'r')
    except IOError:
        return None
    f.close()
    return f

if __name__=='__main__':
    print(try_open('../test/paper.txt'))