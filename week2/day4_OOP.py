class Person:

    def __init__(self, name):
        self.name = name


class Bike:

    def __init__(self, speeds, owner):
        self.speed = speeds
        self.owner = owner
        self.color = ["grey"]
        self._layer = 1

    def set_color(self, new_color):
        self._layer += 1
        self.color.append(new_color)

    def get_color(self):
        return sorted(self.color)

    def get_layer(self):
        return self._layer

joel = Person("Joel")
sean = Person("Sean")

bike = Bike(100, joel)
seans_bike = Bike(18, sean)
# bike.color = "red"
print(bike.owner.name)
print(seans_bike.owner.name)

print(bike)
print("color before change")
print(bike.get_color())
print(bike.get_layer())

print("and after")
bike.set_color("green")
# print(bike.color)
print(bike.get_color())
