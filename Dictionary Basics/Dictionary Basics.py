
jko = {}
jko['Name'] = 'Jason'
jko['Age'] = 31
jko['Country of Birth'] = 'USA'
jko['Favorite Language'] = 'English'

print jko

'''def dictionaryBasics():
    for key, value in jko.items():
        print ("My " + str(key) + " is " + str(value))

dictionaryBasics()'''

def dictionaryBasics2(dict):
    for key, value in dict.items():
        print "My {} is {}".format(key,value)

dictionaryBasics2(jko)