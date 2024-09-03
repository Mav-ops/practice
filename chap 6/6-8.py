# 用列表过于头痛，最后放弃使用字典了
numdict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
           9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
           16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
           50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 200: 'two hundred',
           300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred',
           800: 'eight hundred', 900: 'nine hundred'}


def twonum(number):
    if int(number) < 20:
        return numdict[int(number)]

    elif int(number) > 20 and int(number) % 10 != 0:  ###非10的整数倍
        ten = numdict[int(number[0]) * 10]
        one = numdict[int(number[1])]
        return "%s-%s" % (ten, one)

    return numdict[int(number)]  ##10的整数倍，直接return字典里的


def threenum(number):
    if int(number) % 100 != 0:    ###  非整百
        hundred = numdict[int(number[0]) * 100]

        if int(number[1:]) < 20:     ###119，118，106，104....
            return "%s-%s" % (hundred, numdict[int(number[1:])])

        elif int(number[1:]) > 20 and int(number[1:]) % 10 != 0:  ###321，122，136...
            ten = numdict[int(number[1]) * 10]
            one = numdict[int(number[2])]
            return "%s-%s-%s" % (hundred, ten, one)

        return "%s-%s" % (hundred, numdict[int(number[1:])])  ###120，320，650...

    return numdict[int(number)]  ###100，200，300....


if __name__ == '__main__':
    number = input("Number: ")
    if len(number) <= 2:
        print(twonum(number))
    else:
        print(threenum(number))