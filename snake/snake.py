import pygame
pygame.init()
from random import randint

### MAIN PROGRAM ###
class Main:
    def __init__(self):
        while True:
            self.Game = Snake()

### SNAKE ###
class Snake:
    def __init__(self):
        ### SCREENSIZE ###
        self.width = 400
        self.height = 240
        self.size = (self.width,self.height)
        self.scale = 20  ## Width and height must be dividable by scale ##

        ### GAMEDISPLAY ###
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        ### COLORS ###
        self.background = (255,255,150)
        self.white = (255,255,255)
        self.green = (0,255,0)
        self.red = (255,0,0)
        self.blue = (0,0,255)

        ### SNAKE ###
        self.headimg = pygame.image.load('img/snakehead.png')
        self.appleimg = pygame.image.load('img/apple.png')
        self.GameExit = False
        self.GameOver = False
        self.length = 2
        self.positions = []
        self.xMax = ((self.width / 2) - 10) / 10
        self.yMax = ((self.height / 2) - 10) / 10

        self.MainLoop()

    def DrawSnake(self,direction):
        for pos in self.positions[:-1]:
            pygame.draw.rect(self.screen, self.blue, [pos[0],pos[1],self.scale,self.scale])

        snakehead = self.headimg
        if direction == 'up':
            snakehead == self.headimg
        elif direction == 'down':
            snakehead = pygame.transform.rotate(self.headimg, 180)
        elif direction == 'left':
            snakehead = pygame.transform.rotate(self.headimg, 90)
        elif direction == 'right':
            snakehead = pygame.transform.rotate(self.headimg, 270)

        self.screen.blit(snakehead,(self.positions[-1][0],self.positions[-1][1]))

    def DrawApple(self,x,y):
        #pygame.draw.rect(self.screen, self.red, [x,y,self.scale,self.scale])
        self.screen.blit(self.appleimg,(x-2,y-2))

    def get_pos(self,n):
        return (n * self.scale)

    def check_snake_x(self,x):
        if x >= self.width:
            return 0
        elif x < 0:
            return self.width - 20
        else:
            return x

    def check_snake_y(self,y):
        if y >= self.height:
            return 0
        elif y < 0:
            return self.height - 20
        else:
            return y

    def add_pos(self,x,y):
        SnakeHead = []
        SnakeHead.append(x)
        SnakeHead.append(y)
        self.positions.append(SnakeHead)

    def reset_game(self):
        self.positions = []
        self.length = 2
        self.GameOver = True

    def GameLoop(self):
        self.GameOver = False
        head_x = self.width / 2
        head_y = self.height / 2
        x_change = 0
        y_change = 0
        direction = ''

        apple_x = self.get_pos(randint(0,self.xMax))
        apple_y = self.get_pos(randint(0,self.yMax))

        while not self.GameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m or event.key == pygame.K_BACKSPACE:
                        self.GameOver = True
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        if y_change == 0:
                            x_change = 0
                            y_change = -self.scale
                            direction = 'up'
                            break
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if y_change == 0:
                            x_change = 0
                            y_change = self.scale
                            direction = 'down'
                            break
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if x_change == 0:
                            y_change = 0
                            x_change = -self.scale
                            direction = 'left'
                            break
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if x_change == 0:
                            y_change = 0
                            x_change = self.scale
                            direction = 'right'
                            break

            self.screen.fill(self.background)

            head_x += x_change
            head_y += y_change
            
            head_x = self.check_snake_x(head_x)
            head_y = self.check_snake_y(head_y)

            self.add_pos(head_x,head_y)

            if len(self.positions) > self.length:
                del self.positions[0]

            self.DrawApple(apple_x,apple_y)
            self.DrawSnake(direction)

            pygame.display.update()

            if head_x == apple_x and head_y == apple_y:
                self.length += 1
                apple_x = self.get_pos(randint(0,self.xMax))
                apple_y = self.get_pos(randint(0,self.yMax))

                while True:
                    found = 0
                    for pos in self.positions:
                        if pos == [apple_x,apple_y]:
                            found += 1
                            break
                    if found == 0:
                        break
                    else:
                        apple_x = self.get_pos(randint(0,self.xMax))
                        apple_y = self.get_pos(randint(0,self.yMax))

       
            if self.length > 2:
                for pos in self.positions[:-1]:
                    if pos == [head_x,head_y]:
                        self.reset_game()

            self.clock.tick(15)

    def MainLoop(self):
        self.GameExit = False
        while not self.GameExit:
            self.GameLoop()

Main = Main()