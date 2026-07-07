from kivy.uix.widget import Widget
from kivy.graphics import Color, Triangle, Rectangle
from kivy.core.window import Window


class Player(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Tamaño de la nave
        self.size = (50, 70)

        # Posición inicial (centro de la pantalla)
        self.pos = (
            Window.width / 2 - self.size[0] / 2,
            Window.height / 2 - self.size[1] / 2
        )

        self.speed = 320

        # Dibujar la nave
        with self.canvas:
            # Cuerpo
            Color(0.2, 0.8, 1)
            self.body = Triangle()

            # Ala izquierda
            Color(0.1, 0.5, 1)
            self.left_wing = Triangle()

            # Ala derecha
            Color(0.1, 0.5, 1)
            self.right_wing = Triangle()

            # Cabina
            Color(0.9, 1, 1)
            self.cabin = Rectangle()

            # Motor
            Color(1, 0.5, 0)
            self.engine = Rectangle()

        self.update_graphics()

    def move(self, direction, dt):
        self.x += direction.x * self.speed * dt
        self.y += direction.y * self.speed * dt

        # Limitar a la pantalla
        self.x = max(0, min(self.x, Window.width - self.width))
        self.y = max(0, min(self.y, Window.height - self.height))

        self.update_graphics()

    def update_graphics(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height

        # Cuerpo principal
        self.body.points = [
            x + w / 2, y + h,
            x,         y,
            x + w,     y
        ]

        # Ala izquierda
        self.left_wing.points = [
            x,
            y + h * 0.45,
            x - 10,
            y + 8,
            x + 12,
            y + 10
        ]

        # Ala derecha
        self.right_wing.points = [
            x + w,
            y + h * 0.45,
            x + w + 10,
            y + 8,
            x + w - 12,
            y + 10
        ]

        # Cabina
        self.cabin.pos = (
            x + w * 0.38,
            y + h * 0.45
        )

        self.cabin.size = (
            w * 0.24,
            h * 0.22
        )

        # Motor
        self.engine.pos = (
            x + w * 0.42,
            y - 6
        )

        self.engine.size = (
            w * 0.16,
            8
        )