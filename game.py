from classiq import *

def display_elements():
    for entity in collide_sprite_group:
        entity.display()

    for character in character_sprite_group:
        character.display()

def generateMap():

    for j in range(12):
        for i in range(10):
            if j%2==0:
                cube = Cube("0063",cube_x_offset*i*2,cube_y_offset*j)
            else : 
                cube = Cube("0063",cube_x_offset+cube_x_offset*i*2,cube_y_offset*j)
            addCollideGroup(cube)
    
def start():
    emptyGroup()

    player = Player()
    addCharacterGroup(player)

    generateMap()
    
    list_bot = []
    for i in range(4):
        bot = Bot()
        list_bot.append(bot)
        addCharacterGroup(bot)

    frame_count = 0

    state_game = 0

    while state_game == 0:

        for event in pygame.event.get():
            player.controls(event)

        player.update()

        camera.x =  player.pos.x - WIDTH/2
        camera.y =  player.pos.y-128 - HEIGHT/2

        for bot in list_bot:
            if frame_count%10==0:
                bot.move()
            bot.update()

        screen.blit(cloud_bg,(0,0))

        display_elements()

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1

    return state_game



