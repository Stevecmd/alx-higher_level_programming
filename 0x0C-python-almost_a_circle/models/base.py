import json

class Base:
    """
    Base class to manage id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base.

        Args:
            id (int): If provided, assigns the id to the instance.
                      If not provided, increments __nb_objects and
                      assigns the new value to id.
        """
        if id is not None:
            if id < 0:
                raise ValueError("id must be a non-negative integer")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(list_dicts)
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries represented by json_string.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
