import pygame

class Snake:

    ghostPosition = False

    def __init__(self):
        self.length = 1
        self.speed = 20
        self.direction = 'RIGHT'
        self.coordinates = [(400, 300)]
        self.color = (255,255,255)
        self.alive = False

    def eatApple(self):
        self.length += 1
        print(ghostPosition)
        self.coordinates.append(ghostPosition)
        print(self.coordinates)

    def move(self):
        global ghostPosition
        ghostPosition = self.coordinates[-1]
        for index in range(self.length -1, 0, -1):
            self.coordinates[index] = self.coordinates[index  - 1]

        headX, headY = self.coordinates[0]
        if self.direction == "UP":
            headY -= self.speed
        if self.direction == "DOWN":
            headY += self.speed
        if self.direction == "RIGHT":
            headX += self.speed
        if self.direction == "LEFT":
            headX -= self.speed

        self.coordinates[0] = (headX, headY)

        print(self.coordinates)

    def die(self):
        if self.coordinates[0][1] <= 0 or self.coordinates[0][1] >= 800 or self.coordinates[1][1] <= 0 or self.coordinates[1][1] >= 400
            self.alive = False


    def draw(self, screen):
        for coordinate in self.coordinates:
            x,y = coordinate
            #print(self.coordinates[0])
            pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 16, 16 ))
        self.move()