def taxes(earnmoney, percent = 0.05):
    tax = earnmoney * percent
    return tax
if __name__ == '__main__':
    earnmoney = int(input("Input your earn money number: "))
    print(taxes(earnmoney))