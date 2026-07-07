from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.vector import Vector

from player import Player


class Game(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Actualizar a 60 FPS
        Clock.schedule_interval(self.update, 1 / 60)

        # Jugador
        self.player = Player()
        self.add_widget(self.player)

        # Joystick
        self.joystick_center = (120, 120)
        self.joystick_radius = 70

        self.touch_id = None
        self.move_vector = Vector(0, 0)

        # Dibujar joystick
        with self.canvas:
            Color(0.25, 0.25, 0.25, 0.45)
            self.base = Ellipse(
                pos=(
                    self.joystick_center[0] - self.joystick_radius,
                    self.joystick_center[1] - self.joystick_radius
                ),
                size=(
                    self.joystick_radius * 2,
                    self.joystick_radius * 2
                )
            )

            Color(0.2, 0.8, 1, 0.9)
            self.stick = Ellipse(
                pos=(
                    self.joystick_center[0] - 30,
                    self.joystick_center[1] - 30
                ),
                size=(60, 60)
            )

    def on_touch_down(self, touch):

        if touch.x < Window.width / 2:
            self.touch_id = touch.uid
            self.move_stick(touch)

        return True

    def on_touch_move(self, touch):

        if touch.uid == self.touch_id:
            self.move_stick(touch)

        return True

    def on_touch_up(self, touch):

        if touch.uid == self.touch_id:

            self.touch_id = None
            self.move_vector = Vector(0, 0)

            self.stick.pos = (
                self.joystick_center[0] - 30,
                self.joystick_center[1] - 30
            )

        return True

    def move_stick(self, touch):

        dx = touch.x - self.joystick_center[0]
        dy = touch.y - self.joystick_center[1]

        v = Vector(dx, dy)

        if v.length() > self.joystick_radius:
            v = v.normalize() * self.joystick_radius

        self.move_vector = v / self.joystick_radius

        self.stick.pos = (
            self.joystick_center[0] + v.x - 30,
            self.joystick_center[1] + v.y - 30
        )

    def update(self, dt):

        self.player.move(self.move_vector, dt)