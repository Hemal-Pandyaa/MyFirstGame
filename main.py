import pygame
import colors
import functions

pygame.mixer.init()
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 450
Gamewindow = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


# functions 
def drawSnake(display,color,coords,size):
    for x,y in coords:
        pygame.draw.rect(display,color,[x,y,size,size])



def gameLoop():
    # Game variables 
    exitGame = False
    gameOver = False
    snakeX = SCREEN_WIDTH/2
    snakeY = SCREEN_HEIGHT/2
    snakeSize = 20
    velocityX = 0
    velocityY = 0
    fps = 45
    foodX = functions.getRandX(SCREEN_WIDTH)
    foodY = functions.getRandX(SCREEN_HEIGHT)
    foodSize = 10
    score = 0
    snakeLength = 0
    with open("highScore.txt","r") as f:
        highScore = f.read()

    clock = pygame.time.Clock()

    snakeSegments = [(snakeX,snakeY)]
    head = []



    while not exitGame:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocityX = 5
                    velocityY = 0
                if event.key == pygame.K_LEFT:
                    velocityX = -5
                    velocityY = 0
                if event.key == pygame.K_UP:
                    velocityY = -5
                    velocityX = 0
                if event.key == pygame.K_DOWN:
                    velocityY = 5
                    velocityX = 0

        snakeX += velocityX
        snakeY += velocityY

        if snakeX >= SCREEN_WIDTH:
            snakeX = 0
        elif snakeX <= 0:
            snakeX = SCREEN_WIDTH

        if snakeY >= SCREEN_HEIGHT:
            snakeY = 0
        elif snakeY <= 0:
            snakeY = SCREEN_HEIGHT

        if abs(snakeX - foodX) < snakeSize and abs(snakeY - foodY) < snakeSize:
            score += 1
            foodX = functions.getRandX(SCREEN_WIDTH)
            foodY = functions.getRandX(SCREEN_HEIGHT)
            snakeLength += 5
            if score > int(highScore):
                highScore = score

        head = (snakeX,snakeY)
        
        if head in snakeSegments[:-1]:
            gameOver = True

        snakeSegments.append((head[0],head[1]))

        if(len(snakeSegments) > snakeLength):
            snakeSegments.pop(0)

        Gamewindow.fill(colors.white)

        pygame.draw.circle(Gamewindow,colors.brown,[foodX,foodY],foodSize)
        drawSnake(Gamewindow,colors.green,snakeSegments,snakeSize)
        text = functions.renderText("Score : " + str(score) + ", HighScore : " + str(highScore), colors.red,None)
        Gamewindow.blit(text,[15,15])
        pygame.display.update()

        clock.tick(fps)

        if gameOver:
            # Display game over text and wait for Enter key
            Gamewindow.fill(colors.white)
            with open("highScore.txt","w") as f:
                f.write(str(highScore))
            text = functions.renderText("Game Over! Press Enter to start over", colors.red,None)
            Gamewindow.blit(text, [SCREEN_WIDTH/2 -300, SCREEN_HEIGHT/2])
            pygame.display.update()
            
            waiting_for_enter = True
            while waiting_for_enter:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exitGame = True
                        waiting_for_enter = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            # Reset game variables and start a new game
                            snakeX = 450
                            snakeY = 300
                            snakeSize = 20
                            velocityX = 0
                            velocityY = 0
                            foodX = functions.getRandX(SCREEN_WIDTH)
                            foodY = functions.getRandX(SCREEN_HEIGHT)
                            score = 0
                            snakeLength = 0
                            snakeSegments = [(snakeX, snakeY)]
                            gameOver = False
                            waiting_for_enter = False
    

gameLoop()
pygame.quit()
quit()