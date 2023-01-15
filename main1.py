import pgzero
import pgzrun
import pygame
from pgzero.actor import Actor
import random

WIDTH = 600
HEIGHT = 800

class Paddle:

    def __init__(self):
        self.actor = Actor('puddle.png', center=(WIDTH // 2, HEIGHT - 50))

    def update(self, ball):
        if self.actor.colliderect(ball.actor):
            ball.dy = -ball.dy
            ball.dx = ball.dx if random.randint(0, 1) else -ball.dx

    def draw(self):
        self.actor.draw()


class Ball:

    def __init__(self, speed=-2):
        self.actor = Actor('ball.png', center=(WIDTH // 2, HEIGHT//2))
        self.speed = speed
        self.dx = self.speed
        self.dy = self.speed


    def update(self):
        self.actor.x += self.dx
        self.actor.y += self.dy

        if not (0 <= self.actor.x <= WIDTH):
            self.dx = -self.dx

        if not (0 <= self.actor.y <= HEIGHT):
            self.dy = -self.dy

        if self.actor.y == HEIGHT:
            global hearts
            if len(hearts) != 0:
                del hearts[-1]
            else:
                hearts = [Actor('gameover.png',center=(WIDTH // 2, HEIGHT//2))]
            self.actor.y = HEIGHT // 2
            self.actor.x = WIDTH // 2


    def draw(self):
        self.actor.draw()

class Heart:

    def __init__(self, x):
        self.actor = Actor('heart.png', center=(30*x + 15, 20))

    def draw(self):
        self.actor.draw()



paddle = Paddle()
ball = Ball()

hearts = []
for i in range(3):
    hearts.append(Heart(i))

def draw():
    screen.clear()
    paddle.draw()
    ball.draw()

    for heart in hearts:
        heart.draw()

def update(dt):
    ball.update()
    paddle.update(ball)

def on_mouse_move(pos):
    x, y = pos
    paddle.actor.x = x


pgzrun.go()