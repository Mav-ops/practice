
import time
from time import time,ctime
import string

y=string.digits+string.ascii_letters
db ={}

def newuser():
    prompt ='login desired,only accept digits and letters: '
    while True:
        name =input(prompt).lower()
        if name in y:
            if name in db:
                prompt = 'name taken,try another: '
                continue
            else:
                break
        else:
            print('Invalid name!')
    pwd1 =input('passwd: ')   #明文密码
    logt=time()
    pwd2=pwd1.encode() #密文密码
    db[name] =[pwd2,logt]    #存储密文密码和时间

def olduser():
    name =input('login: ').lower()
    pwd =input('passwd: ')
    if name in db:
        p2=db[name][0].decode()  #解密所存密文
        if pwd ==p2:
            print('welcome back',name)
            current=time()
            delta=current-db[name][1]
            if delta<=10:    #设定10秒，方便测试 4hours=14400s
                print('you already logged in 4 hours period!')
            else:
                print('you last time logged in at:',ctime(db[name][1]))
            logt = time()
            db[name.lower()][1] = logt
        else:
            print('password incorrect')
    else:
         # 当输入的用户名和密码不是注册过的，打印提升信息：是否注册？
        w = input('register it(Y/N)?').strip()[0].lower()
        if 'y' == w:
            newuser()  # 若选择注册，调用新用户注册函数
        else:
            print('login incorrect')

def userlog():
    olduser()


def deluser():
    Getusername()
    c=input('delete a user,its name:').lower()
    if c in db.keys():
        del db[c]
        print('delete completed,the list after deleting:')
        Getusername()
    else:
        print('No such a user!')

def Getusername():
    if db:
        for name in db.keys():
            print("user's name:",name,'pwd:',db[name][0])
    else:
        print('No user!')
def management():
    prompt="""
(D)elete a user
(G)et all user and pwd
(Q)uit

Enter choice:"""
    while True:
        while True:
            try:
                choice=input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice='q'
            print('\nYou picked:[%s]'%choice)

            if choice not in 'gdq':
                print('invalid menu option,try again')
            else:
                break
        if choice=='q':break
        if choice=='g':Getusername()
        if choice=='d':deluser()

def showmenu():
    prompt ="""
(U)ser Login
(M)anage User
(Q)uit

Enter choice:"""

    #done = False
    while True:     #while not done:

        #chosen = False
        while True:   #while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked:[%s]' % choice)
            if choice not in 'uqm':
                print('invalid option,try again')
            else:
                break   ##chosen = True

        if choice == 'q': break  ##done = True
        if choice == 'u': userlog()
        if choice == 'm': management()

if __name__=='__main__':
    showmenu()
