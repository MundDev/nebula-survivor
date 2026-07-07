"""
Nebula Survivor
Archivo principal.
Inicia la aplicación.
"""

from kivy.app import App
from kivy.core.window import Window

from game import Game


class NebulaSurvivor(App):

    def build(self):

        Window.clearcolor = (
            0.02,
            0.02,
            0.05,
            1
        )

        self.title = "Nebula Survivor"

        return Game()


if __name__ == "__main__":

    NebulaSurvivor().run()