from initialisation import *

cube_x_offset = 53
cube_y_offset = 31

camera = vec(0,0)

collide_sprite_group = pygame.sprite.Group()
character_sprite_group = pygame.sprite.Group()

def emptyGroup():
    collide_sprite_group.empty()
    character_sprite_group.empty()

def addCollideGroup(enity):
    enity.add(collide_sprite_group)

def addCharacterGroup(character):
    character.add(character_sprite_group)

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