class Circle:
    def __init__(self, radius):
        self._radius = radius  # Note the use of the underscore as a naming convention for "protected" attributes

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    @radius.deleter
    def radius2(self):
        print("Deleting the radius attribute")
        del self._radius

circle = Circle(5)
print(circle.radius)
del circle.radius2

# # Accessing attributes using the @property decorator
print(circle.radius)    # Accessing radius as a property
# print(circle.diameter)  # Calculated using a property
# print(circle.area)      # Calculated using a property
#
# # Modifying attributes using the setter method
# circle.radius = 7
# print(circle.radius)  # Accessing the modified radius
#
# # Attempting to set a negative radius will raise a ValueError
# circle.radius = -3  # Raises a ValueError
