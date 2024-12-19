from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class Character
    """
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """
    Stark class, inherits from Character
    """
    def __init__(self, name, is_alive=True):
        """
        Init stark class
        name mandatory
        is_alive default True, non mandatory
        """
        self.name = name
        self.is_alive = is_alive if is_alive is True else False

    def die(self):
        """
        Changes is_alive value from True to False
        """
        self.is_alive = False
