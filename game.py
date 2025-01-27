from classiq import *

def display_elements(first_cube,player,list_bot):
    first_cube.display()

    player.display()

    for bot in list_bot:
        bot.display()
    
def start():
    emptyGroup()

    player = Player()

    first_cube = Cube("0060")
    addCollideGroup(first_cube)

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

        display_elements(first_cube,player,list_bot)

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1

    return state_game



