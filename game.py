from Classiq import *

def display_elements(room,player,list_bot):
    #room
    room.display()

    #player
    player.display()

    for bot in list_bot:
        bot.display()
    
def start():
    emptyGroup()

    player = Player()

    room = Room("garden")
    addCollideGroup(room)

    list_bot = []
    for i in range(4):
        bot = Bot(room)
        list_bot.append(bot)

    frame_count = 0

    state_game = 0

    while state_game == 0:

        for event in pygame.event.get():
            player.controls(event)

        player.update()

        for bot in list_bot:
            if frame_count%10==0:
                bot.move(room)
            bot.update()

        screen.fill((0,0,0))

        display_elements(room,player,list_bot)

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1

    return state_game



