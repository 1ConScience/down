import pygame
from pygame.locals import *
import random
import sys

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

vec = pygame.math.Vector2 #2 for two dimensional

FPS = 60

deadzone = 0.3#for joystick
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((0, 0),pygame.NOFRAME,32)

pygame.mouse.set_visible(False) # Hide cursor here

pygame.display.set_caption("Down")

infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h



character_standing_sheet_surf = pygame.image.load("assets/character/neonblue&purple_8direction_standing-Sheet.png").convert_alpha()
walk_EAST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_EAST-Sheet.png").convert_alpha()
walk_NORTH_EAST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_NORTH-EAST-Sheet.png").convert_alpha()
walk_NORTH_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_NORTH-Sheet.png").convert_alpha()
walk_NORTH_WEST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_NORTH-WEST-Sheet.png").convert_alpha()
walk_SOUTH_EAST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_SOUTH-EAST-Sheet.png").convert_alpha()
walk_SOUTH_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_SOUTH-Sheet.png").convert_alpha()
walk_SOUTH_WEST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_SOUTH-WEST-Sheet.png").convert_alpha()
walk_WEST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_WEST-Sheet.png").convert_alpha()
character_mask = pygame.image.load("assets/character/mask2.png").convert_alpha()

character_standing_sheet_surfRED = pygame.image.load("assets/character/red_8direction_standing-Sheet.png").convert_alpha()
walk_EAST_SheetRED = pygame.image.load("assets/character/red_walk_EAST-Sheet.png").convert_alpha()
walk_NORTH_EAST_SheetRED = pygame.image.load("assets/character/red_walk_NORTH-EAST-Sheet.png").convert_alpha()
walk_NORTH_SheetRED = pygame.image.load("assets/character/red_walk_NORTH-Sheet.png").convert_alpha()
walk_NORTH_WEST_SheetRED = pygame.image.load("assets/character/red_walk_NORTH-WEST-Sheet.png").convert_alpha()
walk_SOUTH_EAST_SheetRED = pygame.image.load("assets/character/red_walk_SOUTH-EAST-Sheet.png").convert_alpha()
walk_SOUTH_SheetRED = pygame.image.load("assets/character/red_walk_SOUTH-Sheet.png").convert_alpha()
walk_SOUTH_WEST_SheetRED = pygame.image.load("assets/character/red_walk_SOUTH-WEST-Sheet.png").convert_alpha()
walk_WEST_SheetRED = pygame.image.load("assets/character/red_walk_WEST-Sheet.png").convert_alpha()

character_standing_sheet_surf = pygame.transform.scale(character_standing_sheet_surf, (800,150))
walk_EAST_Sheet = pygame.transform.scale(walk_EAST_Sheet, (800,150))
walk_NORTH_EAST_Sheet = pygame.transform.scale(walk_NORTH_EAST_Sheet, (800,150))
walk_NORTH_Sheet = pygame.transform.scale(walk_NORTH_Sheet, (800,150))
walk_NORTH_WEST_Sheet = pygame.transform.scale(walk_NORTH_WEST_Sheet, (800,150))
walk_SOUTH_EAST_Sheet = pygame.transform.scale(walk_SOUTH_EAST_Sheet, (800,150))
walk_SOUTH_Sheet = pygame.transform.scale(walk_SOUTH_Sheet, (800,150))
walk_SOUTH_WEST_Sheet = pygame.transform.scale(walk_SOUTH_WEST_Sheet, (800,150))
walk_WEST_Sheet = pygame.transform.scale(walk_WEST_Sheet, (800,150))

character_standing_sheet_surfRED = pygame.transform.scale(character_standing_sheet_surfRED, (800,150))
walk_EAST_SheetRED = pygame.transform.scale(walk_EAST_SheetRED, (800,150))
walk_NORTH_EAST_SheetRED = pygame.transform.scale(walk_NORTH_EAST_SheetRED, (800,150))
walk_NORTH_SheetRED = pygame.transform.scale(walk_NORTH_SheetRED, (800,150))
walk_NORTH_WEST_SheetRED = pygame.transform.scale(walk_NORTH_WEST_SheetRED, (800,150))
walk_SOUTH_EAST_SheetRED = pygame.transform.scale(walk_SOUTH_EAST_SheetRED, (800,150))
walk_SOUTH_SheetRED = pygame.transform.scale(walk_SOUTH_SheetRED, (800,150))
walk_SOUTH_WEST_SheetRED = pygame.transform.scale(walk_SOUTH_WEST_SheetRED, (800,150))
walk_WEST_SheetRED = pygame.transform.scale(walk_WEST_SheetRED, (800,150))










collide_sprite_group = pygame.sprite.Group()
enemies_sprite_group = pygame.sprite.Group()

def emptyGroup():
    collide_sprite_group.empty()
    enemies_sprite_group.empty()

def addCollideGroup(test_room):
    test_room.add(collide_sprite_group)

def areSpritesColliding(sprite1,sprite2):
    if sprite1 and sprite2 :
        hit = pygame.sprite.collide_mask(sprite1, sprite2)
        if hit :
            return True
        else :
            return False
    else :
        return False

class Text(pygame.sprite.Sprite):
    def __init__(self,txt,color,size,pos, font = 'Lucida Console'):
        super().__init__()  

        my_font = pygame.font.SysFont(font, size)
        self.surf = my_font.render(txt, False, color)
        self.rect = self.surf.get_rect(center = pos)

    def display(self):
        screen.blit(self.surf, (self.rect.x, self.rect.y))

class AnimatedObject(pygame.sprite.Sprite):
    def __init__(self,name,frames,freq,pos):
        super().__init__()  

        self.sheet = pygame.image.load("assets/objects/"+name+".png").convert_alpha()

        self.w_frame = self.sheet.get_width() / frames
        self.h_frame = self.sheet.get_height()

        self.surf = self.sheet.subsurface((0,0,self.w_frame,self.h_frame))
        self.rect = self.surf.get_rect(center = pos)

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames = freq #that define how many seconds or frames should pass before switching image.

        self.frames_number = frames

        self.mask = pygame.mask.from_surface(self.surf)

    def animate(self):
        self.surf = self.sheet.subsurface((self.w_frame*self.index_frame,0,self.w_frame,self.h_frame))

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= self.frames_number :
                self.index_frame = 0

    def display(self,animation=True):
        if animation :
            self.animate()
        screen.blit(self.surf, (self.rect.x, self.rect.y))