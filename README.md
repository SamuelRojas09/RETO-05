# RETO 5 – Módulos y Paquetes en Python

## Programación Orientada a Objetos – UNAL

Este proyecto consiste en reorganizar el código del sistema de figuras geométricas usando módulos y paquetes en Python. El reto fue desarrollado de dos maneras diferentes:

1. Forma 1: Un único módulo dentro del paquete `Shape`.
2. Forma 2: Múltiples módulos separados, uno por clase.

---

# Forma 1 – Un único módulo

## Estructura

```text
RETO-5.Forma1/
│
├── Shape/
│   ├── __init__.py
│   └── shapes.py
│
└── main.py
```

## Explicación

En esta primera solución se creó un paquete llamado `Shape`.

Dentro del paquete se utilizó un único módulo llamado `shapes.py`, el cual contiene todas las clases del sistema geométrico:

* Point
* Line
* Shape
* Rectangle
* Square
* Triangle
* Equilateral
* Isosceles
* Scalene
* RightTriangle

El archivo `main.py` se dejó separado para realizar todas las pruebas del programa.

---

## Funcionamiento

El archivo `main.py` importa todas las clases desde:

```python
from Shape.shapes import (
    Point,
    Line,
    Shape,
    Rectangle,
    Square,
    Triangle,
    Equilateral,
    Isosceles,
    Scalene,
    RightTriangle
)
```

Luego se crean diferentes figuras geométricas para probar:

* áreas
* perímetros
* ángulos internos
* validaciones
* regularidad

---

## Ventajas de esta forma

* Organización básica del proyecto.
* Código centralizado en un único módulo.
* Fácil de entender para proyectos pequeños.
* Separación entre lógica y pruebas.

---

# Forma 2 – Módulos individuales

## Estructura

```text
RETO-5.Forma2/
│
├── Shape/
│   ├── __init__.py
│   ├── equilateral.py
│   ├── isosceles.py
│   ├── line.py
│   ├── point.py
│   ├── rectangle.py
│   ├── right_triangle.py
│   ├── scalene.py
│   ├── shape.py
│   ├── square.py
│   └── triangle.py
│
└── main.py
```

---

## Explicación

En esta segunda solución se reorganizó completamente el proyecto usando módulos individuales.

Cada clase fue separada en su propio archivo Python.

Por ejemplo:

* `point.py` contiene la clase `Point`
* `line.py` contiene la clase `Line`
* `triangle.py` contiene la clase `Triangle`
* `square.py` contiene la clase `Square`

Esto permite una mejor organización y mantenimiento del código.

---

## Imports utilizados

Se utilizaron imports absolutos para comunicar los módulos entre sí.

Ejemplo:

```python
from Shape.point import Point
```

```python
from Shape.triangle import Triangle
```

---

## Uso de `__name__ == "__main__"`

El archivo principal utiliza:

```python
if __name__ == "__main__":
```

Esto permite ejecutar las pruebas solamente cuando `main.py` es ejecutado directamente.

---

# Resultados obtenidos

El programa permite:

* calcular distancias entre puntos
* calcular longitudes de líneas
* calcular áreas
* calcular perímetros
* calcular ángulos internos
* verificar figuras regulares
* validar tipos especiales de triángulos

---
