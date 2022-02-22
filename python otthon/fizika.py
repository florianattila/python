class Unit:
    def __init__(self, value, unit) -> None:
        self._value = value
        self._unit = unit

    @property
    def value(self):
        return self._value

    def __str__(self) -> str:
        self._magnitude = abs(self._value)
        if self._magnitude > 0:
            if self._magnitude < 0.000000000000000001:
                return f"{self._value * 1000000000000000000000:.3f}z{self._unit}"
            elif self._magnitude < 0.000000000000001:
                return f"{self._value * 1000000000000000000:.3f}a{self._unit}"
            elif self._magnitude < 0.000000000001:
                return f"{self._value * 1000000000000000:.3f}f{self._unit}"
            elif self._magnitude < 0.000000001:
                return f"{self._value * 1000000000000:.3f}p{self._unit}"
            elif self._magnitude < 0.000001:
                return f"{self._value * 1000000000:.3f}n{self._unit}"
            elif self._magnitude < 0.001:
                return f"{self._value * 1000000:.3f}µ{self._unit}"
            elif self._magnitude < 1:
                return f"{self._value * 1000:.3f}m{self._unit}"
            elif self._magnitude < 1000:
                return f"{self._value:.3f}{self._unit}"
            elif self._magnitude < 1000000:
                return f"{self._value / 1000:.3f}k{self._unit}"
            elif self._magnitude < 1000000000:
                return f"{self._value / 1000000:.3f}M{self._unit}"
            elif self._magnitude < 1000000000000:
                return f"{self._value / 1000000000:.3f}G{self._unit}"
            elif self._magnitude < 1000000000000000:
                return f"{self._value / 1000000000000:.3f}T{self._unit}"
            elif self._magnitude < 1000000000000000000:
                return f"{self._value / 1000000000000000:.3f}P{self._unit}"
            else:
                return f"{self._value / 1000000000000000000:.0f}E{self._unit}"

#Feszültség
class Voltage(Unit):
    def __init__(self, value):
        super().__init__(value, "V")
    
    def __add__(self, other): # Defines what happens when you add two objects with the + operator. When you call o1 + o2, under the hood you are calling o1. __add__(o2).
        if type(other) == int or type(other) == float: #__radd__ ellentéte
            return Voltage(self.value + other)
    
    def _iadd__(self, other): # +=
        return self._add__(other)
    
    def __mult__(self, other): #szorzás
        if type(other) == int or type(other) == float:
            return Voltage(self.value*other)
        elif type(other) == Current:
            return Power(self.value * other.value)
    
    def __imul__(self, other): # *=
        return self.__mult__(other)
    
    def __div__(self,other):
        if other.value != 0:
            return Voltage(self.value / other)
        else:
            return "Nullával nem lehet osztani!"
    def __idiv__(self,other):
        return self.__div__(other)
        

#Áram
class Current(Unit):
    def __init__(self, value):
        super().__init__(value, "A")

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Current(self.value+other)

    def __iadd__ (self, other):
        return self.__add__(other)

    def __mul__ (self, other):
        if type(other) == Voltage:
            return Power(self.value * other.value)
        elif type(other) == int or type(other) == float:
            return Current(self.value*other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __div__(self,other):
        if other.value != 0:
            return Current(self.value / other)
        else:
            return "Nullával nem lehet osztani!"

    def __idiv__(self,other):
        return self.__div__(other)
        

#Teljesítmény
class Power(Unit):
    def __init__(self, value):
        super().__init__(value, "W")

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Power(self.value+other)

    def __iadd__ (self, other):
        return self.__add__(other)

    def __mul__ (self, other):
        if type(other) == int or type(other) == float:
            return Power(self.value*other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __div__(self,other):
        if other.value != 0:
            return Power(self.value / other)
            # W = AV
            #
            #
        else:
            return "Nullával nem lehet osztani!"

    def __idiv__(self,other):
        return self.__div__(other)
        
#Teszt
feszultseg = Voltage(50.1)
aram = Current(0.4)
aram2 = Current(63)
aram2 = aram2 * 10
#teljesítmény = feszultseg * aram
print(feszultseg)
print(aram)
print(aram2)
#print(teljesítmény)