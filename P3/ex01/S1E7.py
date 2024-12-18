from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.
    """
    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hairs="dark"):
        """
        Init stark class
        name mandatory
        is_alive default True, non mandatory
        """
        self.first_name = first_name
        self.is_alive = is_alive if is_alive is True else False
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        """
        Changes is_alive value from True to False
        """
        self.is_alive = False


class Lannister(Character):
    """
    Representing the Lannister family.
    """
    def __init__(self, first_name, is_alive=True, family_name="Lannister", eyes="blue", hairs="light"):
        """
        Init stark class
        name mandatory
        is_alive default True, non mandatory
        """
        self.first_name = first_name
        self.is_alive = is_alive if is_alive is True else False
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        """
        Changes is_alive value from True to False
        """
        self.is_alive = False


    def create_lannister(first_name, is_alive):
        """
        Create a lannister with given first_name and is_alive
        """
        return Lannister(first_name, is_alive)