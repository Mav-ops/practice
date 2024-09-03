import os

def newfile():
    symbol=True
    while symbol:
        filename=input('Enter a filename:')
        if os.path.exists(filename):
            print('file is exists.')
        else:
            symbol1=True
            while symbol1:
                content=input('Enter content("q" for quit):')
                if content=='q':
                    break
                f1=open(filename,'a')
                f1.write(content)
                f1.write('\n')
                f1.close()
                symbol=False

def showfile():
    symbol=True
    while symbol:
        filename=input('Enter a filename:')
        if not os.path.exists(filename):
            print('file is not exists.')
        else:
            f1=open(filename,'r')
            for line in f1:
                print(line,end='')
            f1.close()
            break


def editfile():
    symbol=True
    while symbol:
        filename=input('Enter a filename:')
        if not os.path.exists(filename):
            print('file is not exists.')
        else:
            index=int(input('edit index of line:'))
            con=input('Enter edit content:')
            ls=[]
            f=open(filename,'r')
            ls=f.readlines()
            f.close()
            try:
                ls[index-1]=con
            except(IndexError):
                print('the line is out of range,add a new line')
                ls.append(con)
            f1=open(filename,'w')
            for line in ls:
                f1.write(line)
            f1.close()
            symbol=False

def showmenu():
    prompt="""
Menu:
    
(N)ewfile
(S)howfile
(E)ditfile
(Q)uit

Enter choice:"""

    done=True
    while done:
        chosen=True
        while chosen:
            try:
                choice=input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice='q'
            print('\nYou picked:[%s]'%choice)
            if choice not in 'nesq':
                print('invalid option,try again')
            else:
                chosen=False

        if choice=='q':break
        if choice=='n':newfile()
        if choice=='s':showfile()
        if choice=='e':editfile()

if __name__=='__main__':
    showmenu()