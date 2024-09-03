import string


def statitic():
    str=input('enter a sentence:')
    count1=0
    count2=0
    count_word=0
    count_word=len(str.split())
    for i in str:
        if i in 'aeiouAEIOU':
            count1+=1
        else:
            if i in string.ascii_letters:
                count2+=1

    return (count1,count2,count_word)

print(statitic())
