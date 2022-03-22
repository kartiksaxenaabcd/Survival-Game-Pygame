
import pygame
import sprites
import random
import variables
from time import time


def random_generator(die_type,modifier=0,integer=1):
    """ (num,num,int) -> num)
    Random number generator, outputs integers by default."""
    if integer == 0:
        value = random.random()*die_type + modifier
    else:
        value = int(random.random()*die_type) + int(modifier)
    return value

pygame.init()

size = variables.screensize
screen = pygame.display.set_mode(size)
pygame.display.set_caption(variables.gametitle)

background = pygame.Surface(size).convert()
background.fill(variables.bgcolour)

screen.blit(background, (0, 0))

font = pygame.font.Font("trebucbd.ttf", 13)

# Set all screen states.
intro_screen = True
game_initialise = False
game_running = False
end_screen = False
start_initialise = True
running = True

# Start pygame clock
clock = pygame.time.Clock()


while running:


    while intro_screen:
        clock.tick(60)

        if start_initialise:
            # Declare and preset all intro_screen variables.
            startimg = sprites.menuimage(screen, "ui", "start.png")
            menugroup = pygame.sprite.Group()
            menugroup.add(startimg)
            menugroup.clear(screen, background)
            menugroup.draw(screen)
            enter = 0
            start_initialise = False

        # Counts number of times enter is pressed. If enter is used to move onto
        # the next screen.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("Quitting...")
                menugroup.clear(screen, background)
                for img in menugroup:
                        img.kill()
                intro_screen = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_RETURN) and enter == 0:
                    enter = enter + 1
                    menugroup.clear(screen, background)
                    startimg.kill()
                    startimg = sprites.menuimage(screen, "ui", "start1.png")
                    menugroup.add(startimg)
                    menugroup.draw(screen)
                elif event.key == (pygame.K_RETURN) and enter == 1:
                    menugroup.clear(screen, background)
                    for img in menugroup:
                        img.kill()
                    menugroup = pygame.sprite.Group()
                    game_initialise = True
                    enter = 0
                    intro_screen = False
        
        pygame.display.flip()


    if game_initialise:
        
        # Create background and image and group
        backgroundimg = sprites.backgroundimage(screen)
        background_loop = pygame.sprite.Group(backgroundimg)

        # Create player sprite, player group and empty monster group.
        player = sprites.player_animal(screen,"panimal","player02.png")
        player_animal = pygame.sprite.Group(player)
        enemy_animalies = pygame.sprite.Group()

        # Create UI sprites and group
        eatindicate = sprites.menuimage(screen, "ui", "eatindicate02.png", (25, 15), True)
        menugroup.add(eatindicate)

        # All variables (p)reset and declared.
        starttime = time()
        animalmovenum = 1 + variables.enemyvelocity
        animalmovetick = 0
        animalexist = False
        updatetup = ()
        input_list = {pygame.K_w:0, pygame.K_a:1, pygame.K_s:0, pygame.K_d:1,
                      pygame.K_UP:0, pygame.K_LEFT:1, pygame.K_DOWN:0, pygame.K_RIGHT:1}
        vyvx = [[0,0],[0,0]] #[w,s],[a,d]
        pvel = variables.playervelocity
        allrates = variables.enemyanimaltypespawn
        game_initialise = False
        game_running = True

        pygame.display.flip()
        

    while game_running:
        clock.tick(30)

        # Read WASD, arrow keys and Esc, and acts accordingly.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("Quitting...")
                enemy_animalies.clear(screen, background)
                player_animal.clear(screen, background)
                background_loop.clear(screen, background)
                menugroup.clear(screen, background)
                for img in enemy_animalies:
                    img.kill()
                for img in player_animal:
                    img.kill()
                for img in background_loop:
                    img.kill()
                for img in menugroup:
                    img.kill()
                game_running = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_w) or event.key == (pygame.K_UP) :
                        vyvx[0][0] = -pvel
                if event.key == (pygame.K_a) or event.key == (pygame.K_LEFT):
                        vyvx[1][0] = -pvel
                if event.key == (pygame.K_s) or event.key == (pygame.K_DOWN):
                        vyvx[0][1] = pvel
                if event.key == (pygame.K_d) or event.key == (pygame.K_RIGHT):
                        vyvx[1][1] = pvel
            if event.type == pygame.KEYUP:
                for keyname in input_list:
                    if event.key == keyname:
                        vyvx[input_list[keyname]] = [0,0]

        # Randomly spawn animal of a random type depending on rates in variables.enemyanimaltypespawn.
        # Adds to enemy_animalies group.
        spawn = random_generator(1000,-1000 + (10 * variables.enemyanimalpawnrate)) 
        if  spawn > 0:
            if player.weight < allrates[8][0]:
                for line in allrates:
                    if line[0] > player.weight:
                        break
                spawnrates = allrates[allrates.index(line)]
            if player.weight >= allrates[8][0]:
                spawnrates = allrates[8]

            rates = spawnrates[1:11]
            variables.enemyanimalpawnrate = spawnrates[11]
            tmp = random_generator(10,0,0)
     
            for r in rates:
                if tmp < r:
                    break
            animalnum = rates.index(r)
            
            animal = sprites.enemy_animal(screen, "eanimal", variables.animalfiles[animalnum],
                                      velocity=(random_generator(1,1,0),random_generator(1,1,0)))
            enemy_animalies.add(animal)
            animalexist = True
        animalmovetick += 1

        # Creates a new background image, if current background is ending.
        for image in background_loop:
            if image.imagerepeat:
                backgroundimg = sprites.backgroundimage(screen, position=(size[0],0))
                background_loop.add(backgroundimg)
        
        enemy_animalies.clear(screen, background)
        player_animal.clear(screen, background)
        background_loop.clear(screen, background)
        menugroup.clear(screen, background)

        # Update all sprites
        background_loop.update(size)
        if animalmovetick == animalmovenum and animalexist:
            for eanimal in enemy_animalies:
                updatetup = eanimal.update(size,player_animal,player.weight)
                if updatetup != None:
                    player.enemy_collision(updatetup[0],updatetup[1]) # [0] = weight, [1] = nutrition
                    for sizetup in variables.player_animal_size:
                        if sizetup[0] > player.weight:
                            break
                    player.update_image("panimal", "player"+sizetup[1]+".png")
                    eatindicate.update_image("ui", "eatindicate"+sizetup[1]+".png")
                    
        if player.alive:
            # If player does not lose game, continue game.
            if vyvx != [[0,0],[0,0]]:
                player_animal.update(size,vyvx)
            background_loop.draw(screen)        
            enemy_animalies.draw(screen)
            player_animal.draw(screen)

            # Reset animalmovetick to keep animal movement slower.
            if animalmovetick == animalmovenum:
                animalmovetick = 0

            # Update UI bar
            score = player.weight - 20
            text = font.render(str(score) + " grams", True, (255, 255, 255))
            pygame.draw.line(screen, (0,25,50), (5,25), (size[0]-5,25), 40)
            screen.blit(text,(700, 18))
            menugroup.draw(screen)
            
        # If player dies, all items cleared off screen.
        if player.alive == False:
            pygame.time.delay(1000)
            for sprite in enemy_animalies:
                sprite.kill()
            for img in background_loop:
                img.kill()
            for img in menugroup:
                img.kill()
            game_running = False
            end_screen = True
            end_initialise = True
            win = False

        # If score is over or equal to variables.endscore, set win to True
        # and stop running game.
        if score >= variables.endscore:
            pygame.time.delay(1000)
            for sprite in enemy_animalies:
                sprite.kill()
            for img in background_loop:
                img.kill()
            for img in menugroup:
                img.kill()
            gametime = starttime - time()
            print(gametime)
            win = True
            game_running = False
            end_screen = True
            end_initialise = True


        pygame.display.flip()


    while end_screen:
        clock.tick(60)
        
        while end_initialise:
            # Initialise deeat screen with background and "restart" highlighted
            # by default.
            if win:
                endimg = sprites.menuimage(screen, "ui", "win.png")
            else:
                endimg = sprites.menuimage(screen, "ui", "dead.png")
            menugroup.add(endimg)
            endselection = sprites.menuimage(screen, "ui", "restart.png", position=(500,160))
            selectiongroup = pygame.sprite.Group(endselection)
            selection = "restart"
            end_initialise = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_screen = False
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_UP:
                    # Toggle between "restart" and "quit" being highlighted.
                    endselection.kill()
                    selectiongroup.clear(screen, background)
                    if selection == "restart":
                        selection = "quit"
                        endselection = sprites.menuimage(screen, "ui", "quit.png", position=(500,160))
                    elif selection == "quit":
                        selection = "restart"
                        endselection = sprites.menuimage(screen, "ui", "restart.png", position=(500,160))
                    selectiongroup.add(endselection)
                        
                if event.key == pygame.K_RETURN:
                    if selection == "restart":
                        # Enter when "restart" highlighted, resets variables and starts from beginning of running loop.
                        print("Restarting...")
                        start_initialise = True
                        intro_screen = True
                        end_screen = False
                        menugroup.clear(screen, background)
                        selectiongroup.clear(screen, background)
                        for img in menugroup:
                            img.kill()
                        for img in selectiongroup:
                            img.kill()
                    elif selection == "quit":
                        # Kill all sprites on screen, quit all loops, show blank screen/close.
                        print("Quitting...")
                        menugroup.clear(screen, background)
                        selectiongroup.clear(screen, background)
                        for img in menugroup:
                            img.kill()
                        for selectionimg in selectiongroup:
                            selectionimg.kill()
                        event = pygame.QUIT
                        running = False
                        end_screen = False
           
        menugroup.draw(screen)
        selectiongroup.draw(screen)
        
        pygame.display.flip()

