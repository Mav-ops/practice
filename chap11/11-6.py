def printf(arg, *nkw):
    print([arg % eachNum for eachNum in nkw])


printf('%d', 2, 3.4, 5)
printf('%f', 2, 3.4, 5)