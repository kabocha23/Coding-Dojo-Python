class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def Walk(self):
        self.health -= 1
        # print self.health
        return self

    def Run(self):
        self.health -= 5
        # print self.health
        return self

    def DisplayHealth(self):
        print self.health
        return self

giraffe = Animal("Fido",100)

# giraffe.Walk().Walk().Walk().Run().Run().DisplayHealth()

class dog(Animal):
    def __init__(self):
        self.health = 150

    def Pet(self):
        self.health += 5
        return self

dog1 = dog()

# dog1.Walk().Walk().Walk().Run().Run().Pet().DisplayHealth()

# dog1.Fly().DisplayHealth()
# confirmed dog has no method Fly


class dragon(Animal):
    def __init__(self):
        self.health = 170

    def Fly(self):
        self.health -= 10
        return self

    def DisplayHealth(self):
        super(dragon,self).DisplayHealth();
        print "I am a Dragon"

dragon1 = dragon()

# dragon1.Walk().Walk().Walk().Run().Run().Fly().DisplayHealth()


class rabbit(Animal):
    def __init__(self):
        self.health = 20

    def EatCarrot(self):
        self.health += 10
        return self

    def DisplayHealth(self):
        super(rabbit,self).DisplayHealth();
        print "I am a Rabbit"

rabbit1 = rabbit()

# rabbit1.Walk().EatCarrot().Walk().Run().Run().DisplayHealth()
# confirmed new rabbit

# rabbit1.Pet().DisplayHealth()
# confirmed rabbit has no method Pet()

# rabbit1.Fly().DisplayHealth()
# confirmed rabbit has no method Fly()


