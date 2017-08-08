
'''Part I'''
def draw_stars(lst):
    for i in lst:
        a = ""
        for j in range(0,i):
            a += "*" 
        print a

x = [4, 6, 1, 3, 5, 7, 25]

draw_stars(x)

'''Part II'''
def draw_stars(lst):
    for i in lst:
        a = ""
        if isinstance(i,int):
            for j in range(0,i):
                a += "*" 
            print a
        else:
            print (i[0].lower() * len(i))   

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(y)