from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # latest position of the bool = Current velocity + current position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# update - moving the ball by calling the move() and other stuff
class PongGame(Widget):
    ball = ObjectProperty(None)

    def server_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()


class PongApp(App):
    def build(self):
        game = PongGame()
        game.server_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()