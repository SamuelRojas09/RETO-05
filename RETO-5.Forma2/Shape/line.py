from Shape.point import Point    
    
    
# ===================== LINE =====================
# Representa un segmento de línea entre dos puntos
class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self._start = start  # Punto inicial
        self._end = end      # Punto final

    # -------- GETTERS --------
    def get_start(self) -> Point:
        return self._start

    def get_end(self) -> Point:
        return self._end

    # -------- SETTERS --------
    def set_start(self, start: Point) -> None:
        self._start = start

    def set_end(self, end: Point) -> None:
        self._end = end

    # Calcula la longitud del segmento
    def length(self) -> float:
        return self._start.distance_to(self._end)