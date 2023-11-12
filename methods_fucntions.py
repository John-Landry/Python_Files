"""In Python, the main difference between a function and a method is how they are defined and how they are invoked.

A function is a block of reusable code that performs a specific task. It can be defined outside of a class and can be called directly without the need for an object instance. For example:

```python
def greet(name):
    print("Hello,", name)

greet("Alice")
```

In the above code, `greet` is a function that takes a `name` parameter and prints a greeting message.

On the other hand, a method is a function that is defined within a class and is accessed through an object instance or the class itself. When a method is invoked, it operates on the specific instance of the class it belongs to. For example:

```python
class Person:
    def greet(self, name):
        print("Hello,", name)

person = Person()
person.greet("Alice")
```

In this code, `greet` is a method defined within the `Person` class. It takes a `self` parameter, which represents the current instance of the class (similar to `this` in other languages), and a `name` parameter. To invoke the method, we create an instance of the class (`person`) and call the method on that instance.

So, the key differences can be summarized as:
- Functions are defined outside of classes while methods are defined within classes.
- Functions can be called directly, while methods are called on specific objects or the class itself.
- Methods have an additional first parameter (`self` by convention) that refers to the current instance of the class, allowing them to access instance variables and other methods within the class."""