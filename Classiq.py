from head import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames = 2 #that define how many seconds or frames should pass before switching image.
        self.offset_y_frame = 0
        self.offset_x_frame = 0

        self.index_frame_idle = 0 #that keeps track on the current index of the image list.
        self.current_frame_idle = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames_idle = 8 #that define how many seconds or frames should pass before switching image.
        self.offset_y_frame_idle = 0
        self.offset_x_frame_idle = 0

        self.pos = vec((WIDTH/2,HEIGHT/2+200))
        self.vel = vec(0,0)
        self.last_direction = "walk_EAST_Sheet"

        self.surf = idle_EAST_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        self.mask = pygame.mask.from_surface(character_mask)
        self.rect = self.surf.get_rect()

        self.velocity = 5#6

    def update(self):   
        if self.vel != vec(0,0):
            direction = pygame.math.Vector2.normalize(self.vel)
        else :
            direction = self.vel

        self.pos += direction * self.velocity

        self.rect.midbottom = self.pos

        blocks_hit_list = pygame.sprite.spritecollide(self, collide_sprite_group, False, collided = pygame.sprite.collide_mask)
        if blocks_hit_list:
            pass
        else :
            self.pos -= direction * self.velocity
            self.rect.midbottom = self.pos

    def display(self):
        self.animate()
        screen.blit(self.surf, (self.rect.x-camera.x, self.rect.y-camera.y))

    def animate(self):
        if self.vel.x == 0 and self.vel.y == 0:
            self.idleAnimation()
        if self.vel.x > 0 and self.vel.y == 0:
            self.surf = walk_EAST_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_EAST_Sheet"
        elif self.vel.x > 0 and self.vel.y < 0:
            self.surf = walk_NORTH_EAST_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_NORTH_EAST_Sheet"
        elif self.vel.x == 0 and self.vel.y < 0:
            self.surf = walk_NORTH_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_NORTH_Sheet"
        elif self.vel.x < 0 and self.vel.y < 0:
            self.surf = walk_NORTH_WEST_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_NORTH_WEST_Sheet"
        elif self.vel.x < 0 and self.vel.y == 0:
            self.surf = walk_WEST_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_WEST_Sheet"
        elif self.vel.x < 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_WEST_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_SOUTH_WEST_Sheet"
        elif self.vel.x == 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_SOUTH_Sheet"
        elif self.vel.x > 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_EAST_Sheet.subsurface((256*self.offset_x_frame,256*self.offset_y_frame,256,256))
            self.last_direction = "walk_SOUTH_EAST_Sheet"

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1

            self.offset_x_frame += 1

            if self.index_frame == 6 :
                self.offset_x_frame = 0 
                self.offset_y_frame = 1  
            elif self.index_frame == 12 :
                self.index_frame = 0 
                self.offset_x_frame = 0 
                self.offset_y_frame = 0     

    def idleAnimation(self):
        if self.last_direction == "walk_EAST_Sheet":
            self.surf = idle_EAST_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        elif self.last_direction == "walk_NORTH_EAST_Sheet":
            self.surf = idle_NORTH_EAST_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        elif self.last_direction == "walk_NORTH_Sheet":
            self.surf = idle_NORTH_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        elif self.last_direction == "walk_NORTH_WEST_Sheet":
            self.surf = idle_NORTH_WEST_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        elif self.last_direction == "walk_WEST_Sheet":
            self.surf = idle_WEST_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        elif self.last_direction == "walk_SOUTH_WEST_Sheet":
            self.surf = idle_SOUTH_WEST_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        elif self.last_direction == "walk_SOUTH_Sheet":
            self.surf = idle_SOUTH_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))
        elif self.last_direction == "walk_SOUTH_EAST_Sheet":
            self.surf = idle_SOUTH_EAST_Sheet.subsurface((256*self.offset_x_frame_idle,256*self.offset_y_frame_idle,256,256))

        self.current_frame_idle += 1
        if self.current_frame_idle >= self.animation_frames_idle:
            self.current_frame_idle = 0
            self.index_frame_idle += 1

            self.offset_x_frame_idle += 1

            if self.index_frame_idle == 6 :
                self.offset_x_frame_idle = 0 
                self.offset_y_frame_idle = 1  
            elif self.index_frame_idle == 12 :
                self.offset_x_frame_idle = 0 
                self.offset_y_frame_idle = 2  
            elif self.index_frame_idle == 18 :
                self.offset_x_frame_idle = 0 
                self.offset_y_frame_idle = 3  
            elif self.index_frame_idle == 20 :
                self.index_frame_idle = 0 
                self.offset_x_frame_idle = 0 
                self.offset_y_frame_idle = 0  

class Player(Character):
    def __init__(self):
        super().__init__()  

    def controlsJoystick(self):
        if pygame.joystick.get_count()>0:
            hat = joysticks[0].get_hat(0)
            self.vel.x = hat[0]
            self.vel.y = hat[1] * -1

            axis_pos = joysticks[0].get_axis(0)
            if axis_pos < -1 * deadzone:
                self.vel.x -= 1
            elif axis_pos > deadzone:
                self.vel.x += 1 
            else:
                self.vel.x = 0
            axis_pos = joysticks[0].get_axis(1)
            if axis_pos < -1 * deadzone:
                self.vel.y -= 1
            elif axis_pos > deadzone:
                self.vel.y += 1 
            else:
                self.vel.y = 0

    def controls(self,event):

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.vel.x = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.vel.x = 1 
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                self.vel.y = -1
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.vel.y = 1
        if event.type == pygame.KEYUP:   
            if (event.key == pygame.K_q or event.key == pygame.K_LEFT) or (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                self.vel.x = 0
            if (event.key == pygame.K_z or event.key == pygame.K_UP) or (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                self.vel.y = 0

        self.controlsJoystick()

class Bot(Character):
    def __init__(self):
        super().__init__()  

    def move(self):
        magic_number = random.randint(1,9)
        if magic_number == 1:
            self.vel.x = 1
            self.vel.y = 0
        elif magic_number == 2:
            self.vel.x = -1
            self.vel.y = 0
        elif magic_number == 3:
            self.vel.x = 0
            self.vel.y = 1
        elif magic_number == 4:
            self.vel.x = 0
            self.vel.y = -1
        elif magic_number == 5:
            self.vel.x = 1
            self.vel.y = 1
        elif magic_number == 6:
            self.vel.x = -1
            self.vel.y = -1
        elif magic_number == 7:
            self.vel.x = 1
            self.vel.y = -1
        elif magic_number == 9:
            self.vel.x = -1
            self.vel.y = 1
        elif magic_number == 9:
            self.vel.x = 0
            self.vel.y = 0

class Cube(pygame.sprite.Sprite):
    def __init__(self, identifiant,x_offset=0,y_offset=0):
        super().__init__()  

        self.identifiant = identifiant

        self.surf = pygame.image.load("assets/assets_1024x1024/isometric_"+identifiant+".png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (128,128))

        tmp_room_mask = pygame.image.load("assets/isometric_mask.png").convert_alpha()
        tmp_room_mask = pygame.transform.scale(tmp_room_mask, (128,128))
        self.mask = pygame.mask.from_surface(tmp_room_mask)

        self.rect = self.surf.get_rect(center = (WIDTH/2+x_offset, HEIGHT/2+y_offset))

    def display(self):
        self.animate()
        screen.blit(self.surf, (self.rect.x-camera.x, self.rect.y-camera.y))

    def animate(self):
        pass


        