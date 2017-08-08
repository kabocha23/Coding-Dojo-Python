def scoresGrades(score):
    if score < 60:
        print ("Score: " + str(score) + "; Your grade is F")    
    elif score in range(60,70):
        print ("Score: " + str(score) + "; Your grade is D")
    elif score in range(70,80):
        print ("Score: " + str(score) + "; Your grade is C")
    elif score in range(80,90):
        print ("Score: " + str(score) + "; Your grade is B")      
    elif score in range(90,100):
        print ("Score: " + str(score) + "; Your grade is A")  

import random
x = random.randrange(1,100)

scoresGrades(x)