#!/usr/bin/python3
"""Defines a class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """Reprsent base geometry."""


    def area(self):
        """Area function.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """Validate value.

        Args:
            name (str): The name of the object.
            value (int): The value of the property.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
