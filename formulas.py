print("-----------")
print(len(__import__("re").findall(r"[a-zA-Z]+", "Turmoil has engulfed the Galactic Republic. The\ntaxation of trade routes to outlying star systems is in\ndispute. Hoping to resolve the matter with a blockade of deadly\nbattleships, the greedy Trade Federation has stopped all shipping to\nthe small planet of Naboo. While the congress of the Republic\nendlessly debates this alarming chain of events, the Supreme\nChancellor has secretly dispatched two Jedi Knights, the guardians of\npeace and justice in the galaxy, to settle the conflict")))

print(len("And now for something completely different"))


print([*range(6,10)])

a = [*range(7,10)]
# printing the list using loop
for x in range(len(a)):
    print (a[x], end=" ")