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