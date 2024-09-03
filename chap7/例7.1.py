
db ={}

def newuser():
    prompt ='login desired: '
    while True:
        name =input(prompt)
        if name in db:
            prompt ='name taken,try another: '
            continue
        else:
            break
    pwd =input('passwd: ')
    db[name] =pwd

def olduser():
    name =input('login: ')
    pwd =input('passwd: ')
    passwd =db.get(name)
    if passwd==pwd:
        print('welcome back',name)
    else:
        print('login incorrect')

def showmenu():
    prompt ="""
(N)ew User Login
(E)xisting User Login
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
            if choice not in 'neq':
                print('invalid option,try again')
            else:
                break   ##chosen = True

        if choice == 'q': break  ##done = True
        if choice == 'n': newuser()
        if choice == 'e': olduser()

if __name__=='__main__':
    showmenu()
