import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Moving Square')


class Player():
    def __init__(self, x, y, speed, size, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color

    def render(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def up(self):
        self.y = self.y - self.speed
        return self.y

    def down(self):
        self.y = self.y + self.speed
        return self.y

    def left(self):
        self.x = self.x - self.speed
        return self.x

    def right(self):
        self.x = self.x + self.speed
        return self.x


x = 200
y = 200
speed = 0.1
size = 50
color = (0, 0, 0)

player = Player(x, y, speed, size, color)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
        y = player.up()
    if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
        y = player.down()
    if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
        x = player.left()
    if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
        x = player.right()

    screen.fill((255, 255, 255))

    player.render()

    pygame.display.flip()

pygame.quit()
