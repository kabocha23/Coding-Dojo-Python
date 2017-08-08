'''Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.'''
'''# Part I - Solution
for i in range(1, 1000):
    if i%2!=0:
        print i

# Part II - Solution
for j in range(5,1000000):
    if j%5==0:
        print j'''

'''Create a program that prints the sum of all the values in the list:''' 
a = [1, 2, 5, 10, 255, 3]
print sum(a)

'''Create a program that prints the average of the values in the list:'''
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)
