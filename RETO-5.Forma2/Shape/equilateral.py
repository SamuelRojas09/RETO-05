from typing import List

from Shape.triangle import Triangle
from Shape.point import Point


# Triángulo equilátero: todos los lados iguales
class Equilateral(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        if not self.is_regular():
            raise ValueError("Not an equilateral triangle")

    def is_regular(self) -> bool:
        return True