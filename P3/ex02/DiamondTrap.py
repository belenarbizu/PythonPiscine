from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """
    Diamond trap with Baratheon and Lannister
    """
    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hairs="dark"):
        self.first_name = first_name
        self.is_alive = is_alive if is_alive is True else False
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    def set_eyes(self, eyes):
        self.eyes = eyes
    
    def set_hairs(self, hairs):
        self.hairs = hairs
    
    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs