import pgzero
import pgzrun
import pygame
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 800

class Paddle:

    def __init__(self):
        self.actor = Actor('puddle.png', center=(WIDTH // 2, HEIGHT - 50))

    def draw(self):
        self.actor.draw()


class Ball:

    def __init__(self, speed=-1):
        self.actor = Actor('ball.png', center=(WIDTH // 2, HEIGHT//2))


    def draw(self):
        self.actor.draw()

paddle = Paddle()
ball = Ball()

def draw():
    pass
    screen.clear()
    paddle.draw()
    ball.draw()


def update(dt):
    pass


def on_mouse_move(pos):
    x, y = pos
    paddle.actor.x = x


pgzrun.go()