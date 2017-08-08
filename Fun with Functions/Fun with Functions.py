'''Odd/Even'''

def odd_even():
    for i in range(1, 2001, 1):
        if i % 2 != 0:
            print ("Number is " + str(i) + ". This is an odd number.")
        else:
            print ("Number is " + str(i) + ". This is an even number.")

odd_even()


'''Multiply'''

def mlt(lst,num):
    for i in range(len(lst)):
        lst[i] *= num
    print lst

x = [1,4,7,9,12]
y = 20

mlt(x,y)

'''Hacker Challenge'''

def hackChal(lst):
    new_list = []
    for i in lst:    
        listinlist = []
        for k in range(0,i):
            listinlist.append(1)
        new_list.append(listinlist)
    print new_list

hackChal([5,2,3])