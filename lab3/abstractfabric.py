class Tree:
    def __init__(self, type):

        if type == "Pine":
            self.trunk = PineTree.trunk
            self.leaves = PineTree.leaves
        elif type == "Oak":
            self.trunk = OakTree.trunk
            self.leaves = OakTree.leaves


    def calcwood(self):
        return self.trunk * 100

    def calcoxygen(self):
        if self.leaves == "green":
            return "a lot"
        elif self.leaves == "yellow":
            return "a little"


class PineTree:
    trunk = 10
    leaves = "green"

class OakTree:
    trunk = 20
    leaves = "yellow"

class locationUSA:
    weight = 100
    salary = 120

class locationChina:
    weight = 60
    salary = 40


class woodcutter:
    def __init__(self, location = "USA"):
        if location == "USA":
            self.salary = locationUSA.salary
            self.weight = locationUSA.weight

        elif location == "China":
            self.salary = locationChina.salary
            self.weight = locationChina.weight


class wood:

    def __init__(self, tree = "Pine", cutter = "USA"):
        self.tree = Tree(tree)
        self.cutter = woodcutter(cutter)
        self.calcwood()

    def calcwood(self):
        self.time = self.tree.calcwood() / self.cutter.weight
        self.amount = self.tree.calcwood()
        self.cost = self.time * self.cutter.salary

    def __str__(self):
        outstr = "Cost is "
        outstr += str(self.cost)
        outstr += "; Time is "
        outstr += str(self.time)
        outstr += "; Amount is "
        outstr += str(self.amount)
        return outstr

getwood1 = wood()

print(getwood1)

getwood2 = wood(tree = "Oak", cutter = "China")

print(getwood2)

