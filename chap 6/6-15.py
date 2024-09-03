from datetime import date
def calculate_date_diff(date1, date2):
    # 将输入的字符串日期转换为date对象
    d1 = date(int(date1[0:4]), int(date1[5:7]), int(date1[8:10]))
    d2 = date(int(date2[0:4]), int(date2[5:7]), int(date2[8:10]))
    # 计算两个日期的差值
    diff = abs((d2 - d1).days)
    return diff
# 调用函数并输出结果
date1=input('YYYY-MM-DD:')
date2=input('YYYY-MM-DD:')
print(calculate_date_diff(date1,date2))  # 输出


'''
import time
 
def calculate_date_diff(date1, date2):
    # 将输入的字符串日期转换为时间元组
    time1 = time.strptime(date1, "%Y-%m-%d")
    time2 = time.strptime(date2, "%Y-%m-%d")
 
    # 将时间元组转换为时间戳
    timestamp1 = time.mktime(time1)
    timestamp2 = time.mktime(time2)
 
    # 计算两个日期的差值，并转换为天数
    diff = abs(timestamp2 - timestamp1) / (24 * 3600)
 
    return diff
 
# 调用函数并输出结果
print(calculate_date_diff("2021-01-01", "2021-01-10"))  # 输出 9.0

'''