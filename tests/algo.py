class Classy(object):
    def __init__(self):
        self.items = []
        self.classpoints = {"tophat": 2, "bowtie": 4, "monocle": 5}


    def calculateclassiness(self):
        self.currentpoint = 0
        if self.items:
            for i in self.items:
                if i in self.classpoints.keys():
                    self.currentpoint += self.classpoints[i]
                    print(i)
                    print(self.currentpoint)

                else:
                    pass
        else:
            return 0

        return self.currentpoint

    def getClassiness(self):
        return self.calculateclassiness()

    def addItem(self, new_items):
        self.items.append(new_items)


# Test cases
me = Classy()

# Should be 0
print
#me.getClassiness()

me.addItem("tophat")
# Should be 2
print
me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print
me.getClassiness()

me.addItem("bowtie")
# Should be 15
print
print(me.getClassiness())
print(me.items)
