import string
import keyword
alphas=string.ascii_letters+'_'
nums=string.digits
print('Welcome to the Identifier Checker v2.0')
print('Testees must be at least 1char long.')
myinput=input('Identifier to test?')
if len(myinput)>1:
    if myinput[0] not in alphas:
        print('invalid:first symbol must be alphabetic')
    else:
        alphnums=alphas+nums
        for otherchar in myinput[1:]:
            if otherchar not in alphnums:
                print('invalid:remaining symbols must be alphanumeric')
                break
        else:
            if myinput in keyword.kwlist:
                print('invalid:the input is the key')
            else:
                print('OKay as an identifier')

else:
    if myinput!='_'and myinput in alphas:
        print('OKay as an identifier')
    else:
        print('is not an identifier')