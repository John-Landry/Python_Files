
str="Hello all!! \nI am Pythoner \nWelcome"
print(str)

print("Hello!! \nI am \nWelc")
print("Hello!! \nI am \nWelc")
print("------------------------")
lst = ['Python','Java\n',"\n" 'Kotlin','Cpp', "\n"]
print("List before adding newline character to it:",lst)
lst = '\n'.join(lst)
print("List after adding newline character to it:\n",lst)

print("------------------------")
print("str1\nstr2")

print("------------------------")
print("str1\nstr2\n.....strN")
print("Hello Folks! Let us start learning.")
print("Statement after adding newline through print() function....")
print("Hello Folks!\nLet us start learning.")

print("------------------------")
newline = '\n'
str = f"Python{newline}Java{newline}Cpp"
print(str)

print("------------------------")


name = "Fred"
print("He said his name is",(name),"\b.")
print("He said his name is " + (name) + ".")
print(f"He said his name is {name}.")
print("He said his \nname is {name}.")
print("He said\t\t his name is (name).")
print("He said his name is name.")

def greet(name):
    print("Hello,", name, "!")
    print(f"Hello, " + name + "!")
    print("Hello, " + name + "!")

greet("Alice")

class Person:
    def greet(self, name):
        print("Hello,", name)

person = Person()
person.greet("Alice,  a method is a function that is defined within a class and is accessed through an object instance or the class itself. When a method is invoked, it operates on the specific instance of the class it belongs to")