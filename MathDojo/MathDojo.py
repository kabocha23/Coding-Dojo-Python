# PART I
# class MathDojo(object):
    
#     def __init__(self):
#         self.result = 0

#     def Add(self,*args):
#         for i in args:
#             self.result += i
#         return self

#     def Subtract(self,*args):
#         x = 0
#         for i in args:
#             x += i
#         self.result = self.result - x 
#         return self
    
#     def Result(self):
#         print self.result
#         return self

# md = MathDojo()

# md.Add(2).Add(2, 5).Subtract(3, 2).Result()

# PART II
# class MathDojo(object):
    
#     def __init__(self):
#         self.result = 0

#     def Add(self,*args):
#         for i in args:
#             if type(i) == list:
#                 for j in i:
#                     self.result += j
#             else:        
#                 self.result += i
#         return self

#     def Subtract(self,*args):
#         x = 0
#         for i in args:
#             if type(i) == list:
#                 for j in i:
#                     self.result += j
#             else:        
#                 x += i
#                 self.result = self.result - x 
#         return self
    
#     def Result(self):
#         print self.result
#         return self

# md = MathDojo()

# md.Add([1],3,4).Add([3, 5, 7, 8], [2, 4.3, 1.25]).Subtract(2, [2,3], [1.1, 2.3]).Result()

# PART III

class MathDojo(object):
    
    def __init__(self):
        self.result = 0

    def Add(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    self.result += j
            else:        
                self.result += i
        return self

    def Subtract(self,*args):
        x = 0
        for i in args:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    self.result += j
            else:        
                x += i
            self.result = self.result - x 
        return self
    
    def Result(self):
        print self.result
        return self

md = MathDojo()

md.Add([1],3,4).Add([3, 5, 7, 8], [2, 4.3, 1.25]).Subtract(2, [2,3], [1.1, 2.3]).Result()