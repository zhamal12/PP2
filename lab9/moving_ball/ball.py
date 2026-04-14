import pygame

class Ball:
    def __init__(self, x, y, radius, speed, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move_left(self):
        if self.x - self.speed - self.radius >= 0:
            self.x -= self.speed

    def move_right(self):
        if self.x + self.speed + self.radius <= self.screen_width:
            self.x += self.speed

    def move_up(self):
        if self.y - self.speed - self.radius >= 0:
            self.y -= self.speed

    def move_down(self):
        if self.y + self.speed + self.radius <= self.screen_height:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)