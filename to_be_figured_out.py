class Sales:
    def __init__(self, id):
        self.id = id
        id = 100

val = Sales(123)
print (val.id)



s = "\t\tWelcome\n"
print(s.strip())



x = 50
 
def func():
    global x
 
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func()
print('The value of x is', x)


w1 = "Hello, world!"
w2 = "I love Python."
w1 = w2
print(w2)
print(w1)
w1 = "Hello, world!"
w2 = "I love Python."
w2 = w1
print(w2)
print(w1)

def f(x = 100, y = 100): 
   return(x+y, x-y) 
x, y = f(y = 200, x = 100) 
print(x, y) 

def f(a, b = 1, c = 2):
   print('a is: ',a, 'b is: ', b, 'c is: ', c)
f(2, c = 2)
f(c = 100, a = 110)