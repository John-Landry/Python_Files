class Saint:

    def __init__(self, name, attribute, patron_of, home, feast_day, manner_of_death ):
        self.name = name
        self.attribute = attribute
        self.patron_of = patron_of
        self.home = home
        self.feast_day = feast_day
        self.manner_of_death = manner_of_death

    def story(self):
        print(self.name + ", whose feast day is "
              + self.feast_day + ", is the patron saint of "
              + self.patron_of + " and is often seen carrying "
              + self.attribute + ". This saint "
              + self.manner_of_death + " and is buried in "
              + self.home + ".")

    def origin(self):
        print(self.name + "'s church is in "
              + self.home + ".")

    def celebrate(self):
        print(self.name + "'feast day is on "
              + self.feast_day + ".")

    def carrying(self):
        print(self.name + " is often seen carrying a "
              + self.attribute + ".")

    def make_line(self):
        print("------------------------------------------------------------")

saint1 = Saint("Joan of Arc",
               "a sword",
               "soldiers",
               "Orleans",
               "May 30",
               "was burned at the stake")

saint2 = Saint("Thomas Aquinas",
               "a pen",
               "students",
               "Toulouse",
               "January 28",
               "keeled over while delivering a sermon")


saint3 = Saint("Sebastian",
               "an arrow",
               "athletes",
               "Rome",
               "January 20",
               "was beaten to death with clubs")

print("------------------------------------------------------------")
saint1.make_line()
saint1.celebrate()
saint2.celebrate()
saint3.celebrate()
saint1.origin()
saint2.origin()
saint3.origin()
saint1.carrying()
saint2.carrying()
saint3.carrying()
saint1.story()
saint2.story()
saint3.story()