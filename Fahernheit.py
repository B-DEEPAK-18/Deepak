# Creating a class as Fahernheit
class Fahernheit:

    # Initialising or defining a function as init
    def __init__(self, temperature=0):
        self.set_temperature = temperature
        print("given Temperature= ", self.set_temperature)

    # Initialising or defining a function as converting  fahrenheit to celsius
    def to_celsius(self):
        return (self.temperature - 32) / 1.8

        # It reads temperature from above function init
        def get_temperature(self):
            return self.temperature

    # Using setter for temperature
    def set_temperature(self, value):
        # Comparing a temparatur to kelvin
        if value < -273:
            raise ValueError("Temperature below -273 not possible")
        self.temperature = value
        temperature = property(get_temperature, set_temperature)

# Calling a above functions
c = Fahernheit()
c.temperature = 37
print(c.to_celsius())
print("after converting from fahrenheit to celsius  :", c.to_celsius())
