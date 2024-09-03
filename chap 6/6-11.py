def ipTransfer(ipaddress):
    """输入整型转换成www.xxx.yyy.zzz格式"""
    transferedIP = []
    if len(ipaddress) != 12:
        return "输入有误"
    else:
        for i in range(len(ipaddress)//3):
            transfer, ipaddress = ipaddress[:3], ipaddress[3:]
            transferedIP.append(transfer)
            ###trabsferedIP=['123','456','789','258']
    return '.'.join(transferedIP)
            ### return 123.456.789.258

def ipreverse(ipaddress):
    if len(ipaddress) != 15:
        return "输入有误"
    else:
        ipaddress = list(ipaddress)
        ## = ['1','2','3','.'          省略...]
        for ch in ipaddress:
            if ch == '.':
                ipaddress.remove(ch)
            ## ipaddress=['1','2','3','4',      省略...]
    return ''.join(ipaddress)
           ## return 123456789258

if __name__ == '__main__':
    ip = input('IP: ')
    print(ipTransfer(ip))
    print(ipreverse(ip))