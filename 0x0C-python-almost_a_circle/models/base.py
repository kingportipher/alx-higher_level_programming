#!/usr/bin/python3

class Base:
    """
    Base class for managing 'id' attributes in future classes.
    """
    def __init__(self, id=None):
        """
        Class constructor.
        Args:
            id (int, optional):
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
