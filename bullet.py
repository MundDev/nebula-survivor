from kivy.graphics import Color, Ellipse

class Bullet:
    ...

class BulletManager:
    ...
class Bullet:
    """
    Bala individual.
    No usa Widget para mejorar rendimiento.
    """

    def __init__(self, canvas):

        self.alive = False

        self.x = 0
        self.y = 0

        self.vx = 0
        self.vy = 0

        self.speed = 650
        self.damage = 10
        self.radius = 6


        with canvas:

            Color(0.2, 1, 1)

            self.shape = Ellipse(
                pos=(-100, -100),
                size=(
                    self.radius * 2,
                    self.radius * 2
                )
            )


    def shoot(self, x, y, direction):

        self.alive = True

        self.x = x
        self.y = y

        self.vx = direction.x * self.speed
        self.vy = direction.y * self.speed

        self.update_graphics()



    def update(self, dt):

        if not self.alive:
            return


        self.x += self.vx * dt
        self.y += self.vy * dt

        self.update_graphics()



    def update_graphics(self):

        if self.alive:

            self.shape.pos = (
                self.x - self.radius,
                self.y - self.radius
            )

        else:

            self.shape.pos = (
                -100,
                -100
            )



    def deactivate(self):

        self.alive = False

        self.update_graphics()



class BulletManager:

    def __init__(self, canvas):

        self.bullets = []


        # Pool de balas

        for _ in range(100):

            self.bullets.append(
                Bullet(canvas)
            )



    def shoot(self, x, y, direction):

        for bullet in self.bullets:

            if not bullet.alive:

                bullet.shoot(
                    x,
                    y,
                    direction
                )

                return



    def update(self, dt, width, height):

        for bullet in self.bullets:

            if not bullet.alive:
                continue


            bullet.update(dt)


            if (
                bullet.x < -20 or
                bullet.x > width + 20 or
                bullet.y < -20 or
                bullet.y > height + 20
            ):

                bullet.deactivate()
                