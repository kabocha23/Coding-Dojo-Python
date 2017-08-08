class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        self.miles += 10
        print "Riding"
        return self

    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        print "Reversing"
        return self

new_bike1 = Bike("$250","25 mph")
new_bike2 = Bike("$300","30 mph")
new_bike3 = Bike("$350","35 mph")


new_bike1.ride()
new_bike1.ride()
new_bike1.ride()
new_bike1.reverse()
new_bike1.displayInfo()

new_bike2.ride()
new_bike2.ride()
new_bike2.reverse()
new_bike2.reverse()
new_bike2.displayInfo()

new_bike3.reverse()
new_bike3.reverse()
new_bike3.reverse()
new_bike3.displayInfo()