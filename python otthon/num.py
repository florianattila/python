class NumString:
    
    def __init__(self, value):
        self.value = str(value)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

some_num1 = NumString(0) # Create an instance of NumString with 0 as value.
str(some_num1) # Check what is contained within self.value in this instance.
# Output: '0'

some_num1 + 1 # We add some_num1 to 1, this returns back the calculation using the __add__ method
str(some_num1) # check what some_num1 is holding for a self.value
# Output: '0'

some_num1 += 2 # We in-place add some_num1 to 2, this stores and returns the new stored value using __iadd__ method.
str(some_num1) # check what some_num1 is holding now?
# Output: '2'