import pygame
import random
import time

RED = (214, 52, 49)
BLACK = (0, 0, 0)

class target:

    def __init__(self):
        self.destroyed = False
        self.x = random.randrange(20, 1880)
        self.y = random.randrange(300, 600)
        self.width = random.randrange(15, 35)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)

    def draw(self, window):
        if(self.destroyed):
            pygame.draw.rect(window, BLACK, self.rect)
        else:
            pygame.draw.rect(window, RED, self.rect)

    def clicked(self, position):
        self.destroyed = self.rect.collidepoint(position)

def main():
    pygame.init()
    window = pygame.display.set_mode((0,0), pygame.RESIZABLE)
    pygame.display.set_caption('Aim Trainer')
    pygame.font.init()

    font = pygame.font.Font('freesansbold.ttf', 30)

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

        if(newTarget.destroyed and count < 50):
            score = font.render("Score: " + str(count), False, BLACK)
            count += 1
            newTarget = target()
            newTarget.draw(window)

        if(count >= 50):
            newTarget.destroyed = True
            newTarget.draw(window)

        currentTime = time.time()
        if(int(currentTime - start) > timeElapsed and count < 50):
            timeText = font.render("Time: " + str(timeElapsed), False, BLACK)
            timeElapsed = int(currentTime - start)

        # event checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                newTarget.clicked(position)
                newTarget.draw(window)

        # window update
        pygame.display.update()
        window.blit(score, (850,20))
        window.blit(timeText, (850, 50))

main()