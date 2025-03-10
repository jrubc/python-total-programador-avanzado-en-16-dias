class Bird:  # Class declaration
    pass

    alas = True  # Class atribute

    def __init__(
        self, color, specie
    ):  # Class constructor, it is used to create a instance of this class
        # self parameter represents the instance that will be created
        self.color = color  # Instance atribute
        self.specie = specie

    # Instance methods
    def piar(self):
        print("pio")

    def fly(self, feets):
        print(f"The {self.specie} has flown {feets} feets")
        self.piar()  # Instance methods can also call other instance methods

    def print_dark(self):
        self.color = "dark"
        print(
            f"Now {self.specie} is dark"
        )  # Instance methods can modify instance atributes

    @classmethod
    def lay_leggs(cls, amount):
        print(f"Bird lay {amount} eggs")
        cls.alas = False  # Cass methods can modify class atributes

    @staticmethod
    def look():  # Static methods can't access to atributes or other methods
        print("Bird looks")


my_bird = Bird("blue", "toucan")
my_bird.piar()
my_bird.fly(10)
my_bird.alas = False
print(my_bird.alas)


# Calling class methods
Bird.lay_leggs(5)

# []
