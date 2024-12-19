from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Diamond trap with Baratheon and Lannister
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """
        Set the color of the eyes
        """
        self.eyes = eyes

    def set_hairs(self, hairs):
        """
        Set the color of the hair
        """
        self.hairs = hairs

    def get_eyes(self):
        """
        Return the color of the eyes
        """
        return self.eyes

    def get_hairs(self):
        """
        Return the color of the hair
        """
        return self.hairs
