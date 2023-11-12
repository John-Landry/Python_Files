def display_person(*args):
    for i in args:
        print(i)

display_person("name","age")


def display_person(**kwargs):
    for i in kwargs:
        print(i)


display_person(name="Emma", age="25")


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)


