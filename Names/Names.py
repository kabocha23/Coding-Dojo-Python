students = [
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def namesAssign(lst):
#     for i in lst:
#         print i["first_name"],i["last_name"]

# namesAssign(students)

'''def namesAssign(lst):
    for i in lst:
        for key in i.iteritems():
            print "first_name", "last_name"

namesAssign(students)'''

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

 
def namesAssign2(dict):
    
    # countIns = 0
    for key, value in dict.iteritems():
        print key
        countStu = 0
        for i in value:
            countStu += 1
            print countStu," - ",i["first_name"],i["last_name"]," - ",(len(i["first_name"])+len(i["last_name"]))





namesAssign2(users)