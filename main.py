import pygame
import random
import time

RED = (214, 52, 49)
BLACK = (0, 0, 0)

class target:

    def __init__(self):
        self.destroyed = False
        self.xSpeed = 0.1
        self.ySpeed = 0.1
        self.x = random.randrange(20, 1880)
        self.y = random.randrange(300, 600)
        self.width = random.randrange(15, 35)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)

    def draw(self, window):
        if(self.destroyed):
            pygame.draw.rect(window, BLACK, self.rect)
        else:
            pygame.draw.rect(window, RED, self.rect)

    def erase(self, window):
        pygame.draw.rect(window, BLACK, self.rect)

    def onTarget(self, position):
        return self.rect.collidepoint(position)

    def move(self, window):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed
        self.erase(window)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)
        self.draw(window)
        if(self.x > 1900):
            self.xSpeed = -0.1
        elif(self.x < 0):
            self.xSpeed = 0.1
        if(self.y < 0):
            self.ySpeed = 0.1
        elif(self.y > 1000):
            self.ySpeed = -0.1


def main():
    pygame.init()
    window = pygame.display.set_mode((0,0), pygame.RESIZABLE)
    pygame.display.set_caption('Aim Trainer')
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 30)

    flickTraining(window, font)
    # trackTraining(window, font)


def trackTraining(window, font):
    running = True
    count = 0
    oldCount = 0
    newTarget = target()
    newTarget.draw(window)

    start = time.time()
    timeElapsed = 0
    # game loop
    while (running):
        score = font.render("Score: " + str(int(count)), False, BLACK)
        score = font.render("Score: " + str(int(count)), False, RED)
        timeText = font.render("Time: " + str(timeElapsed), False, RED)

        newTarget.move(window)
        position = pygame.mouse.get_pos()
        if(newTarget.onTarget(position)):
            oldCount = count
            count += 0.004

        if(int(count) > oldCount):
            score = font.render("Score: " + str(int(oldCount)), False, BLACK)

        currentTime = time.time()
        if (int(currentTime - start) > timeElapsed and count < 50):
            timeText = font.render("Time: " + str(timeElapsed), False, BLACK)
            timeElapsed = int(currentTime - start)

        # event checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # window update
        pygame.display.update()
        window.blit(score, (window.get_width() / 2, 20))
        window.blit(timeText, (window.get_width() / 2, 50))

def flickTraining(window, font):
    running = True
    count = 0
    newTarget = target()
    newTarget.draw(window)

    start = time.time()
    timeElapsed = 0
    # game loop
    while (running):

        score = font.render("Score: " + str(count), False, RED)
        timeText = font.render("Time: " + str(timeElapsed), False, RED)

        if (newTarget.destroyed and count < 50):
            score = font.render("Score: " + str(count), False, BLACK)
            count += 1
            newTarget = target()
            newTarget.draw(window)

        if (count >= 50):
            newTarget.destroyed = True
            newTarget.draw(window)

        currentTime = time.time()
        if (int(currentTime - start) > timeElapsed and count < 50):
            timeText = font.render("Time: " + str(timeElapsed), False, BLACK)
            timeElapsed = int(currentTime - start)

        # event checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                newTarget.destroyed = newTarget.onTarget(position)
                newTarget.draw(window)

        # window update
        pygame.display.update()
        window.blit(score, (window.get_width() / 2, 20))
        window.blit(timeText, (window.get_width() / 2, 50))

main()