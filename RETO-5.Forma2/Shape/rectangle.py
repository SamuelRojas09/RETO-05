from typing import List

from Shape.shape import Shape
from Shape.point import Point
from Shape.line import Line

    
# ===================== RECTANGLE =====================
# Representa un rectángulo
class Rectangle(Shape):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        # Se crean los 4 lados del rectángulo usando los vértices
        self._edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[3]),
            Line(vertices[3], vertices[0]),
        ]

    # Área del rectángulo = base * altura
    def compute_area(self) -> float:
        base = self._edges[0].length()
        height = self._edges[1].length()
        return base * height

    # Todos los ángulos internos de un rectángulo son de 90 grados
    def inner_angles(self) -> List[float]:
        return [90.0, 90.0, 90.0, 90.0]

    # Un rectángulo no es regular (a menos que sea cuadrado)
    def is_regular(self) -> bool:
        return False