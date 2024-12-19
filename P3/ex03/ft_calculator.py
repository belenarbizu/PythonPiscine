class calculator:
    """
    Calculator that can add, multiply, subtract and divide
    """
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object)-> None:
        """
        Add vector and scalar
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object)-> None:
        """
        Multiply vector and scalar
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object)-> None:
        """
        Subtract vector and scalar
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object)-> None:
        """
        Divide vector and scalar
        """
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print("Error:", e)
