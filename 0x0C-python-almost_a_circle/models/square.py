from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance
        
        Args:
            size (int): Size of the square.
            x (int): X coordinate of the square's position.
            y (int): Y coordinate of the square's position.
            id (int): Identifier of the square.None - unique id generated.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
