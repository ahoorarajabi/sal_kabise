year=int(input('sale marboote ra vared konid: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('in sal kabise ast')
else:
    print("in sal kabise nist")