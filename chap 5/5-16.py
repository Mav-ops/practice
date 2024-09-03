def Payment(balance,paid):
    count=0
    print('              Amount   Remaining')
    print('Pymt#           Paid    Banlance')
    print('-----         ------   ---------')
    while True:
        print('%2d        $%.2f          $%6.2f'%(count,paid,balance))
        if balance-paid>=0:
            balance=balance-paid
        else:
            if balance!=0:
                print('%2d        $%.2f          $%6.2f'%(count+1,balance,0))
            break
        count+=1

if __name__=='__main__':
    balance=float(input('balance:'))
    paid=float(input('paid:'))
    Payment(balance,paid)
