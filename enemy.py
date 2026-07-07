from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.vector import Vector


class Enemy(Widget):
    """
    Enemigo básico.
    Persigue al jugador constantemente.
    """

    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)

        self.size = (40, 40)
        self.pos = (x, y)

        self.speed = 140
        self.hp = 10
        self.damage = 10

        with self.canvas:
            # Núcleo
            Color(1, 0.15, 0.15)
            self.core = Ellipse(size=self.size)

            # Anillo exterior
            Color(1, 0.5, 0.5)
            self.ring = Line(circle=(0, 0, 22), width=2)

        self.update_graphics()

    def update(self, dt, player):

        # Dirección hacia el jugador
        direction = Vector(
            player.center_x - self.center_x,
            player.center_y - self.center_y
        )

        if direction.length() > 0:
            direction = direction.normalize()

        self.x += direction.x * self.speed * dt
        self.y += direction.y * self.speed * dt

        self.update_graphics()

    def update_graphics(self):

        self.core.pos = self.pos

        self.ring.circle = (
            self.center_x,
            self.center_y,
            22
        )

    def hit(self, damage):

        self.hp -= damage

        return self.hp <= 0