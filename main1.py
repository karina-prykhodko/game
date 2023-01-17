import pgzero
import pgzrun
import pygame
from pgzero.actor import Actor
import random
from math import sqrt

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

    def __init__(self, speed=-2, radius=20):
        self.actor = Actor('ball.png', center=(WIDTH // 2, HEIGHT//2))
        self.speed = speed
        self.dx = self.speed
        self.dy = self.speed
        self.radius = radius


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


class Obstacle:

    def __init__(self, x , y, radius=30, color='blue'):
        self.pos = x, y
        self.radius = radius
        self.color = color
        self.status = True

    def update(self, ball):
        length = sqrt((self.pos[0] - ball.actor.x)**2 + (self.pos[1] - ball.actor.y)**2)
        if length <= int(self.radius + ball.radius):
            self.status = False
        return self.status


    def draw(self):
        if self.status == True:
            screen.draw.filled_circle(self.pos, self.radius, self.color)
        else:
            pass

def create_obstacles(k = 6, y = 100 ):

    оbstacles_balls = []
    x = WIDTH // k+3
    for i in range(k):
        оbstacles_balls.append(Obstacle(x * i + 45, y))

    for i in range(k-1):
        оbstacles_balls.append(Obstacle(x * i + 90, y+90))

    return оbstacles_balls

paddle = Paddle()
ball = Ball()

hearts = []
for i in range(3):
    hearts.append(Heart(i))

оbstacles = create_obstacles()

def draw():
    screen.clear()
    paddle.draw()
    ball.draw()

    for heart in hearts:
        heart.draw()

    for item in оbstacles:
        item.draw()

def update(dt):
    ball.update()
    paddle.update(ball)
    for item in оbstacles:
        if item.update(ball) == False:
            оbstacles.remove(item)
            ball.dx = -ball.dx
            ball.dy = -ball.dy


def on_mouse_move(pos):
    x, y = pos
    paddle.actor.x = x


pgzrun.go()