import pygame
import random
import math
from pygame import mixer    # its Used for Sound Effects


def inceptionLvlKaFunction():
    global fire_state
    global screen
    global score
    global bulletYposition
    global bulletXPosition
    global bulletY_change
    Rerun = True
    while Rerun:
        score = 0
        # images
        ufo = pygame.image.load('ufo.png')
        goli = pygame.image.load('bullet.png')
        background = pygame.image.load('space.jpg')
        loadImg = pygame.image.load('startImg.jpg')
        chahal_bhai = pygame.image.load('wapis_khelega.jpg')

        # Shuruvat Ka Riti Rivaj
        pygame.init()  # initializes the Pygame
        screen = pygame.display.set_mode((800, 600))
        title = pygame.display.set_caption('SpceInvdrbyGuarav')
        icon = pygame.display.set_icon(ufo)
        mixer.music.load("Background sound.mp3")
        mixer.music.play(-1)

        # Fonts
        font = pygame.font.Font('Mahaputra.ttf', 60)
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        font3 = pygame.font.Font('Mahaputra.ttf', 30)
        font4 = pygame.font.Font('Mahaputra.ttf', 20)
        font5 = pygame.font.Font('freesansbold.ttf', 12)

        # Player
        playerXposition = 420
        playerYposition = 530
        playerX_change = 0
        playerY_change = 0


        def player(x, y):
            screen.blit(ufo, (x, y))


        # Enemy
        def enemyLoop():
            global number_of_enemies
            number_of_enemies = 6
            global enemyImg
            global enemyXposition
            global enemyYposition
            global enemyX_change
            global enemyY_change
            enemyImg = []
            enemyXposition = []
            enemyYposition = []
            enemyX_change = []
            enemyY_change = []
            for i in range(number_of_enemies):
                enemyImg.append(pygame.image.load('alien.png'))
                enemyXposition.append(random.randint(0, 768))
                enemyYposition.append(random.randint(0,50))
                enemyX_change.append(4)
                enemyY_change.append(30)


        def enemyIncLoop():
            global number_of_enemies
            number_of_enemies = number_of_enemies + 1
            enemyImg.append(pygame.image.load('alien.png'))
            enemyXposition.append(random.randint(0, 768))
            enemyYposition.append(random.randint(0, 50))
            enemyX_change.append(4)
            enemyY_change.append(30)

        enemyLoop()

        def enemy(x, y,i):
            screen.blit(enemyImg[i], (x, y))


        # Bullet
        bulletYposition = 560
        fire_state = 'ready'
        bulletY_change = 9


        def iscollision(bx, by, ex, ey, i):
            global score
            global fire_state
            global bulletYposition
            distance = math.sqrt((ex - bx)**2 + (ey - by)**2)       # Calculating Distance between Bullet and Enemy
            if distance < 27:
                collision_sound = mixer.Sound('Explosion.wav')
                collision_sound.play()
                fire_state = 'ready'
                enemyYposition[i] = random.randint(0,50)
                enemyXposition[i] = random.randint(1,750)
                bulletYposition = 500
                score += 1
                # Below codes will Give Comments according to ur score in Console
                if score == 10:
                    print(f'{score}: One Enemy has been increased')
                if score == 20:
                    print(f'{score}: Carefully brother!! One more enemy has been increased')
                if score == 30:
                    print(f'{score}: Playing Well Brother!! Just keep going like this...')
                if score == 50:
                    print(f'{score}: Congrats!!! You made a Half Century')
                if score == 70:
                    print(f'{score}: Now Stop it Brother, till when you will keep playing it.')
                if score == 85:
                    print(f'{score}: Stop it Brother!! Now my game is running out of Codes')
                if score == 100:
                    print(f'{score}: You wont listen to me!! Keep playing it Lifetime!!! The game is in Infinity Loop, it wont end!!!!')
                if ((score != 0) and (score % 10 ==0)):
                    enemyIncLoop()


        def fire(x, y):
            global fire_state
            if fire_state == 'fire':
                screen.blit(goli, (x, y))


        # ................GAme Loop That exits only when red cross of window is clicked........................#
        running = True
        isGameStarted = False
        while running:
            while (not isGameStarted):
                screen.blit(loadImg,(0,0))
                writeupOnLoad1 = font3.render('Press any Key To Start the Game',True,(200,234,140))
                writeupOnLoad2 = font4.render('Except the Power Button of your PCorLAPTOP', True, (70, 70, 70))
                screen.blit(writeupOnLoad1,(250,500))
                screen.blit(writeupOnLoad2, (270, 550))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        Rerun = False
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        isGameStarted = True
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -6
                    if event.key == pygame.K_RIGHT:
                        playerX_change = +6
                    # Game Pause
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        while pause:
                            game_paused = font.render("GAME  PAUSED", True, (0, 255, 0))
                            screen.blit(game_paused, (250, 250))
                            pygame.display.update()
                            for eventP in pygame.event.get():
                                if eventP.type == pygame.QUIT:
                                    exit()
                                if eventP.type == pygame.KEYDOWN:
                                    if eventP.key == pygame.K_ESCAPE:
                                        pause=False
                                else: pass
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        playerX_change = 0
                if event.type == (pygame.KEYDOWN or pygame.MOUSEBUTTONDOWN):
                    if ((event.key == pygame.K_SPACE) or (event.key == pygame.MOUSEBUTTONDOWN)):
                        if fire_state is 'ready':
                            bullet_sound = mixer.Sound('gunfire.wav')
                            bullet_sound.play()
                            bulletXPosition = playerXposition + 16
                            fire_state = 'fire'

            # Player
            playerXposition += playerX_change
            playerYposition += playerY_change
            if playerXposition <= 0:        # Setting up player Boundaries
                playerXposition = 0
            elif playerXposition >= 736:
                playerXposition = 736
            if playerYposition <= 85:
                playerYposition = 85
            elif playerYposition >= 568:
                playerYposition = 568

            # Enemy
            for i in range(number_of_enemies):
                enemyXposition[i] += enemyX_change[i]
                if enemyXposition[i] >= 768:
                    enemyX_change[i] = -4
                    enemyYposition[i] += 30
                elif enemyXposition[i] <= 0:
                    enemyX_change[i] = +4
                    enemyYposition[i] += 30
                if enemyYposition[i] >= 465:
                    running = False
                    chahal_loop = True
                    while chahal_loop:
                        screen.blit(chahal_bhai, (0, 0))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                Rerun = False
                                quit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:
                                    inceptionLvlKaFunction()
                                else: quit()
            # Bullet
            if bulletYposition < -10:
                bulletYposition = 560
                fire_state = 'ready'


            player(playerXposition, playerYposition)
            for i in range(number_of_enemies):
                enemy(enemyXposition[i], enemyYposition[i],i)
            if fire_state is 'fire':
                fire(bulletXPosition, bulletYposition)
                bulletYposition -= bulletY_change
                enemy_bin_list = []
                for i in range(number_of_enemies):
                    enemy_bin_list.append(i)
                for i in enemy_bin_list:
                    iscollision(bulletXPosition, bulletYposition, enemyXposition[i], enemyYposition[i],i )

            score_written = font2.render(("Score:"+ str(score)), True, (150, 100, 5))
            number_of_Enemeies_Written = font5.render(("No. of Enemies: "+ str(number_of_enemies)),True, (150,150,150))
            screen.blit(number_of_Enemeies_Written,(680,5))
            screen.blit(score_written,(20,20))
            pygame.display.update()
        # .............................................GAme loop ends here.............................................#
inceptionLvlKaFunction()
