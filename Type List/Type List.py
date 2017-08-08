'''def typeList(lis):
        stri = ''
        count1 = 0
        added = 0
        count2 = 0
        for i in range(len(lis)):
            if type(i) == str:
                stri += i
                count1 += 1
            elif type(i) == int or type(i) == float:
                added += i
                count2 += 1
        if count1 > 0 and count2 > 0:
            print ('The list You entered is a mixed type')
            print stri
            print added
        elif count1:
            print ('The list You entered is a string type')
            print stri
        elif count2:
            print ('The list You entered is an integer type')
            print added

a = ['magical unicorns',19,'hello',98.98,'world']

typeList(a)'''

def typeList(lis):
        stri = ''
        count1 = 0
        added = 0
        count2 = 0
        for i in lis:
            if type(i) == str:
                stri += i
                count1 += 1
            elif type(i) == int or type(i) == float:
                added += i
                count2 += 1
        if count1 > 0 and count2 > 0:
            print ('The list You entered is a mixed type')
            print stri
            print added
        elif count1:
            print ('The list You entered is a string type')
            print stri
        elif count2:
            print ('The list You entered is an integer type')
            print added

a = ['magical unicorns',19,'hello',98.98,'world']

typeList(a)