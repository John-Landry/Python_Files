my_list = list(("88.1", 88.1, "apple", "banana", "cherry"))
my_list2 = ["100.1",100.1, "owls", "pliers", "tulips"]
my_list3 = list()
my_list4 = []


print(type(my_list))
print(len(my_list))
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

print("---------------------------------------")

my_tuple = tuple(("88.1", 88.1, "apple", "banana", "cherry"))
my_tuple2 = ("88.1", 88.1, "pliers", "tulips")
my_tuple3 = tuple()
my_tuple4 = ()

print(type(my_tuple))
print(len(my_tuple))
print(my_tuple)
print(my_tuple2)
print(my_tuple3)
print(my_tuple4)

print("---------------------------------------")

my_set = set(("88.1", 88.1, "apple", "banana", "cherry"))
my_set2 = {"88.1", 88.1, "owls", "pliers", "tulips"}
my_set3 = set()

print(type(my_set))
print(len(my_set))
print(my_set2)
print(my_set3)

print("---------------------------------------")

my_dict = dict(x12345670000=999.0867600, srgrty89="sky", owls="sky", tulips="singalong")
my_dict2 = {"56pea6ce":"sky", 89:"sky", "456456":56.7654576768, 45646:"sky"}
my_dict3 = dict()
my_dict4 = {}
print(type(my_dict4))
print(type(my_dict))
print(len(my_dict))
print(my_dict)
print(my_dict2)
print(my_dict3)



print("---------------------------------------")
i = int("12345")
r = (123, 987)
p = str("abcdefg,kk")
j = "12345, 90990"
print("---------------------------------------")
k = 1,2,39877
m = list("1,2,3877")
q = [1,2,389]
n = set("john, 123, 45")
o = dict(word=1 , word45462=3)

print("INT", type(i))
print("INT", i)
print("INT", type(r))
print("INT", r)
print("STR", type(p))
print("STR", p)
print("STR", type(j))
print("STR", j)
print("---------------------------------------")
print("TUPLE", type(k))
print("TUPLE", k)
print("LIST", type(m))
print("LIST", m)
print("SET", type(n))
print("SET", n)
print("DICT", type(o))
print("DICT", o)






gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append('pajamas')

print(gift_list)

lst=[11, 100, 101, 999, 1001]
#Type your answer here.

answer_1 = lst[-1]

print(answer_1)


gift_list=['socks', '4K drone', 'wine', 'jam']
gift_list.append('pajamas')

print(gift_list)
print(type({}))


print("--------------")



d = {'foo': 100, 'bar': 200, 'baz': 300}
print(d)
d = dict([
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
])
print(d)
d = dict(foo=100, bar=200, baz=300)

print(d)


d = {
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
}
print(d)
d = {}
print(d)
print(type(d))
d = []
print(d)
print(type(d))
d = ()
print(d)
print(type(d))

d = {
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
}
print(d)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[1:5])          # Output: [2, 3, 4, 5]
print(my_list[::2])          # Output: [1, 3, 5, 7, 9]
print(my_list[1:7:2])        # Output: [2, 4, 6]
print(type(my_list))
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple[1:5])          # Output: [2, 3, 4, 5]
print(my_tuple[::2])          # Output: [1, 3, 5, 7, 9]
print(my_tuple[1:7:2])        # Output: [2, 4, 6]
print(type(my_tuple))
my_string = ("1, 2, 3, 4, 5, 6, 7, 8, 9")
print(my_string[1:5])          # Output: [2, 3, 4, 5]
print(my_string[::2])          # Output: [1, 3, 5, 7, 9]
print(my_string[1:7:2])        # Output: [2, 4, 6]
print(type(my_string))
my_string = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
print(my_string[1:5])          # Output: [2, 3, 4, 5]
print(my_string[::2])          # Output: [1, 3, 5, 7, 9]
print(my_string[1:7:2])        # Output: [2, 4, 6]
print(type(my_string))