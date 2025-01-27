from classiq import *

def display_elements(list_cube,player,list_bot):
    for cube in list_cube:
        cube.display()

    player.display()

    for bot in list_bot:
        bot.display()
    
def start():
    emptyGroup()

    player = Player()

    list_cube = []



    cube3 = Cube("0063",107,-62)
    addCollideGroup(cube3)
    list_cube.append(cube3)

    cube1 = Cube("0063")
    addCollideGroup(cube1)
    list_cube.append(cube1)


    cube4 = Cube("0063",107*2,0)
    addCollideGroup(cube4)
    list_cube.append(cube4)

    cube2 = Cube("0063",107,62)
    addCollideGroup(cube2)
    list_cube.append(cube2)    

    list_bot = []
    for i in range(4):
        bot = Bot()
        list_bot.append(bot)

    frame_count = 0

    state_game = 0

    while state_game == 0:

        for event in pygame.event.get():
            player.controls(event)

        player.update()

        for bot in list_bot:
            if frame_count%10==0:
                bot.move()
            bot.update()

        screen.fill((0,0,0))

        display_elements(list_cube,player,list_bot)

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1

    return state_game



