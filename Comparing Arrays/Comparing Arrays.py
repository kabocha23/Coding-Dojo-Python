

def comparArr(first,second):
    
    first.sort()
    second.sort()
    if first == second:
        print "The lists are the same"
    else:
        print "The lists are not the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,3]

list_three = ['celery','carrots','bread','milk']
list_four = ['celery','carrots','bread','cream']

comparArr(list_one,list_two)