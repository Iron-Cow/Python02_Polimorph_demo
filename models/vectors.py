class Vector:
    """2D Vector"""
    def __init__(self, x: int or float, y: int or float):
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f"({self.__x} ; {self.__y})"

    def get_coords(self) -> tuple:
        return (self.__x, self.__y)

    def __add__(self, other):
        """
        Возвращает сумму векторов по формуле
        Vector(x, y)
        x = x1 + x2
        y = y1 + y2

        (1, 2 - номера векторов self и other

        :param other: Vector
        :return: Vector
        """
        x1, y1 = self.get_coords()
        x2, y2 = other.get_coords()
        x = x1 + x2
        y = y1 + y2

        return Vector(x, y)

    def __sub__(self, other):
        """
        Возвращает разницу векторов по формуле
        Vector(x, y)
        x = x1 - x2
        y = y1 - y2

        (1, 2 - номера векторов self и other

        :param other: Vector
        :return: Vector
        """
        x1, y1 = self.get_coords()
        x2, y2 = other.get_coords()
        x = x1 - x2
        y = y1 - y2

        return Vector(x, y)
