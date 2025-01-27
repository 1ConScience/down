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




walk_EAST_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir6.png").convert_alpha()
walk_NORTH_EAST_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir5.png").convert_alpha()
walk_NORTH_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir4.png").convert_alpha()
walk_NORTH_WEST_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir3.png").convert_alpha()
walk_SOUTH_EAST_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir7.png").convert_alpha()
walk_SOUTH_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir8.png").convert_alpha()
walk_SOUTH_WEST_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir1.png").convert_alpha()
walk_WEST_Sheet = pygame.image.load("assets/for_walk/Fox_Walk_dir2.png").convert_alpha()

character_mask = pygame.image.load("assets/fox_mask.png").convert_alpha()












collide_sprite_group = pygame.sprite.Group()
enemies_sprite_group = pygame.sprite.Group()