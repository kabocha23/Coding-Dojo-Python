# in: two lists containing strings
# out: first list keys second list values, in same dictionary


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    cmp(arr1,arr2)
    new_dict = {}
    new_dict = zip(arr1,arr2)
    # print new_dict     
    new_dict = dict(new_dict)
    print new_dict

make_dict(name,favorite_animal)