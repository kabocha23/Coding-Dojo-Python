class Product(object):
    def __init__(self,price,item_name,weight,brand,cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def addTax(self,tax):
        self.price = round((self.price * tax),2)
        return self

    def Return(self,reason):
        if reason == a:
            self.status = "Defective"
            self.price = 0
        elif reason == b:
            self.status = "For Sale"
        elif reason == c:
            self.status = "Used"
            self.price = round((self.price * .8),2)
        return self
        
    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight) + " oz."
        print "Brand: " + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self.status)

a = "defective"
b = "in_box"
c = "opened"
cards = Product(2.99,"cards",3,"Bicycle",1.50)
Hot_Wheel = Product(3.99,"Corvette",2,"Hot Wheels",1.99)

# cards.addTax(1.09).displayInfo()
cards.addTax(1.084).Return(c).displayInfo()
