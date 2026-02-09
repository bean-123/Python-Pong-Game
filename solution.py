import pygame
pygame.init()

#Defining the display
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255,255,255)
BLACK= (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

#Creating the Paddles
class Paddle:
    COLOR = WHITE
    VEL = 4 #Velocity which the paddle moves when user presses the key

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win): #Drawing the paddles as rectangles
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    #Moving the paddle on Y axel, connection with handle_paddle_movement
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

#Changing the color of the Display
def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles: 
        paddle.draw(win)

    pygame.display.update() #Need to update the display

#Defining the keys
def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    if keys[pygame.K_s]:
        left_paddle.move(up=False)
    
    if keys[pygame.K_UP]:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN]:
        right_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT// 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) #Centering the paddle
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) #Leaving padding on the side

    
    while run:
        clock.tick(FPS) #Adding FPS/clock so it runs at same speed on all PCs
        draw(WIN, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()