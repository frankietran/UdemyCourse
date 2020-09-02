class Fruit(object):
    def __init__(self):
        print("Created a fruit instance")

    def nutrition(self):
        print("Fruit nutrition")

    def fruit_shape(self):
        print("Fruit shape")


class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("Creating an apple instance")

    def nutrition(self):
        print("Apple nutrition")

    def color(self):
        print("Apple color")


f = Fruit()
f.nutrition()
f.fruit_shape()

a = Apple()
a.nutrition()
a.fruit_shape()
a.color()

