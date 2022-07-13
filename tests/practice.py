def decorateBasic(func):
    def newDeco():
        print("Before the execution")
        func()
        print("After the execution")

    return newDeco


def Basicfunc():
    print("Base func")
    Details = {"Destination": "China",
               "Nstionality": "Italian", "Age": []}
    Details["Age"] += [20, "Twenty"]
    print(Details)


# Python | Sort Python Dictionaries by Key or Value

# Create a dictionary and display its keys alphabetically.
# Display both the keys and values sorted in alphabetical order by the key.
# Same as part (ii), but sorted in alphabetical order by the value.

from collections import OrderedDict

d1 = {'samsung': 'M30', 'Diomi': 'X00', 'sony': 'XM90','apple':'A19' }

#print(sorted(d1.keys()))
x1=[]
# x1 = [x for i in sorted((d1.items())]

# xx = OrderedDict(sorted(d1.items()))
# print(xx)