import pygame, sys, asyncio
from random import randint
from pygame.locals import *

##const
MAX_WINDOW = (1280,720)
IMG_MANAGER = {}

##main
async def main():
    pygame.init()
    pygame.mixer.init()
    root = pygame.display.set_mode(MAX_WINDOW, pygame.RESIZABLE)
    #pygame.mixer.music.load("./assets/audio/dukesiraqo.wav")
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.6) 
    window_w, window_h = MAX_WINDOW[0], MAX_WINDOW[1]
    clock = pygame.time.Clock()

    gamestate_manager = Journal()
    

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                window_w, window_h = event.w, event.h
                root = pygame.display.set_mode((window_w, window_h), pygame.RESIZABLE)
        
        gamestate_manager.update_mouse_pos(window_w, window_h)

        #send root to functions; return canvas, blit canvas to root, send root via main once per cycle
        if gamestate_manager.gamestate == "TITLE":
            canvas = scene_title(root, events, gamestate_manager)
        elif gamestate_manager.gamestate == "DRAFT":
            canvas = scene_draft(root, events, gamestate_manager)
        elif gamestate_manager.gamestate == "CREDITS":
            canvas = scene_credits(root, events, gamestate_manager)

        resolution = pygame.transform.scale(canvas, (window_w, window_h))
        root.blit(resolution, (0,0))
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)



##classes
class Draft_Card:
    def __init__(self, x, y, name):
        self.INDENT_SIZE = MAX_WINDOW[0]/5
        self.SPACING_SIZE = 32
        self.INDENT_MICRO = 16
        self.MENU_SIZE = (self.INDENT_SIZE/2, MAX_WINDOW[1]/3-self.SPACING_SIZE)
        self.image = pygame.Surface(self.MENU_SIZE)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.name = name

    def draw_self(self):
        self.image.fill((166,44,10))
        write_textbox(f"{self.name}", 5, 5).draw(self.image)   
        return self.image
    

class Draft_Seat:
    def __init__(self, seat_number):
        self.MENU_SIZE = (MAX_WINDOW[0] - MAX_WINDOW[0]/4, MAX_WINDOW[1]/3)
        self.INDENT_SIZE = MAX_WINDOW[0]/5
        self.SPACING_SIZE = 36
        self.hand_size = 5
        self.canvas = pygame.Surface(self.MENU_SIZE)
        self.seat_num = seat_number #needs to become dynamic for multiplayer
        self.draft_menu = Draft_Menu()
        self.draft_field = Draft_Field()
        self.draft_hand = []
        self.active_card = None
        self.is_active = False

    def load_hand(self, n):
        for _ in range(n):
            self.draft_hand.append(Draft_Card(0, 15, _)) #needs to be random card, but thats later

    def update_hand_rects(self):
        for i, card in enumerate(self.draft_hand):
            card.rect.x = (card.image.get_width()+card.INDENT_MICRO)*i + card.INDENT_MICRO   
            #card.rect.x += (MAX_WINDOW[0]/(self.hand_size+2))*i + card.INDENT_MICRO/3 

    def hand_to_active(self, card):
        self.active_card = card
        self.draft_hand.remove(card)
        self.is_active = True
    def active_to_hand(self):
        self.draft_hand.append(self.active_card)
        self.active_card = None
        self.is_active = False 
    def active_to_field(self):
        self.draft_field.team_bus.append(self.active_card)
        self.active_card = None
        self.is_active = False  

    def hand_interface(self, events, journal):
        mouse_pos = (journal.mouse_pos)
        offset_mouse = (mouse_pos[0] - MAX_WINDOW[0]/4, mouse_pos[1] - MAX_WINDOW[1]*2/3)

        self.canvas.fill((166,190,210))
        pygame.draw.rect(self.canvas, (60,144,177), (0,0,MAX_WINDOW[0],self.SPACING_SIZE/6))

        for card in self.draft_hand:
            if card.rect.collidepoint(offset_mouse):
                pygame.draw.rect(self.canvas, (60,144,177), (card.rect.x-6,card.rect.y-6,
                                                             card.image.get_width()+12,card.image.get_height()+12))
            self.canvas.blit(card.draw_self(), card.rect)

        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if self.is_active == True:
                    self.active_to_hand()
                    self.update_hand_rects()
                if self.is_active == False:
                    for card in self.draft_hand:
                        if card.rect.collidepoint(offset_mouse):
                            self.hand_to_active(card)
                            self.update_hand_rects()
                


        write_textbox(f"hello world {self.MENU_SIZE}", 0, 0).draw(self.canvas)

        return self.canvas
    
class Draft_Menu:
    def __init__(self):
        self.MENU_SIZE = (MAX_WINDOW[0]/4, MAX_WINDOW[1])
        self.INDENT_SIZE = 40
        self.SPACING_SIZE = 36
        self.canvas = pygame.Surface(self.MENU_SIZE)
        self.button_bus = []

    def menu_interface(self, events, journal):
   
        mouse_pos = journal.mouse_pos
        self.canvas.fill((190,210,70))
        pygame.draw.rect(self.canvas, (60,144,177), (self.MENU_SIZE[0]-self.SPACING_SIZE/6,0,self.SPACING_SIZE/6,MAX_WINDOW[1]))

        self.button_bus.append(write_textbox("<QUIT_GAME>", self.INDENT_SIZE, self.SPACING_SIZE))
        self.button_bus.append(write_textbox("<OPTIONS>", self.INDENT_SIZE, self.SPACING_SIZE*2))
        self.button_bus.append(write_textbox("<CREDITS>", self.INDENT_SIZE, self.SPACING_SIZE*3))
        
        for button in self.button_bus:
            if button.rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.canvas, (255,0,0),
                                button.image.get_rect(topleft=(button.rect.x, button.rect.y)))
            button.draw(self.canvas)
        
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                for button in self.button_bus:
                    if button.rect.collidepoint(mouse_pos):
                        if button == self.button_bus[0]:
                            journal.gamestate = "TITLE"
                            journal.seat_bus = []
                        elif button == self.button_bus[2]:
                            journal.gamestate = "CREDITS"
                            

        self.button_bus = []
        return self.canvas

class Draft_Field:
    def __init__(self):
        self.MENU_SIZE = (MAX_WINDOW[0]*3/4, MAX_WINDOW[1]*2/3)
        self.INDENT_SIZE = 40
        self.SPACING_SIZE = 36
        self.canvas = pygame.Surface(self.MENU_SIZE)
        self.button_bus = []
        self.team_bus = []

    def field_interface(self, events, journal):
        mouse_pos = journal.mouse_pos
        active_user = journal.seat_bus[journal.active_seat]
        offset_mouse = (mouse_pos[0] - MAX_WINDOW[0]/4, mouse_pos[1])
        self.canvas.fill((90,210,70))
        
        
        self.button_bus.append(write_textbox("'FIELD'", self.INDENT_SIZE, self.SPACING_SIZE*3))
        
        for button in self.button_bus:
            if button.rect.collidepoint(offset_mouse):
                pygame.draw.rect(self.canvas, (25,144,0),
                                button.image.get_rect(topleft=(button.rect.x, button.rect.y)))
            button.draw(self.canvas)
        
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                print(offset_mouse)
                for button in self.button_bus:
                    if button.rect.collidepoint(offset_mouse) and active_user.is_active == True:
                         active_user.active_to_field()                   

        self.button_bus = []

        for player_card in self.team_bus:
            self.canvas.blit(player_card.draw_self(), (self.MENU_SIZE[0]/2, self.MENU_SIZE[1]/2))

        return self.canvas

class Journal:
    def __init__(self):
        self.gamestate = "TITLE"
        self.mouse_pos = (0,0)
        self.button_bus = []
        self.seat_bus = []
        self.active_seat = 0


    def hand_to_seat(self):
        for seat in self.seat_bus:
            seat.load_hand(seat.hand_size)
    
    def update_mouse_pos(self, window_w, window_h):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        offset_x = MAX_WINDOW[0]/window_w
        offset_y = MAX_WINDOW[1]/window_h

        self.mouse_pos = mouse_x*offset_x, mouse_y*offset_y


class Widget:
    def __init__(self, image_file, x, y):
        self.image = image_file
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        ###takes any image and makesa rectangle
    def draw(self, canvas):
        canvas.blit(self.image, self.rect)


##functions
def collision(class_with_rects, single_target_rect):
    if class_with_rects.rect.colliderect(single_target_rect):
        return True
    return False

def load_image(filename, alpha_bool):
    if filename not in IMG_MANAGER:
        if alpha_bool == True:
            IMG_MANAGER[filename] = pygame.image.load(filename).convert_alpha()
        else:
            IMG_MANAGER[filename] = pygame.image.load(filename).convert()
    ### loads and stores images to prevent lag/repeated loads
    return IMG_MANAGER[filename]

def rng(n):
    return randint(0,n)

def menu_title(events, journal):
    MENU_SIZE = (640,300)
    INDENT_SIZE = 40
    SPACING_SIZE = 36
    mouse_pos = journal.mouse_pos
    offset_mouse = (mouse_pos[0] - MENU_SIZE[0]/2, mouse_pos[1] - MENU_SIZE[1]/2 - SPACING_SIZE-15)
    menu_canvas = pygame.Surface(MENU_SIZE)
    menu_canvas.fill((190,210,70))
    
    journal.button_bus.append(write_textbox("<START_GAME>", INDENT_SIZE, SPACING_SIZE))
    journal.button_bus.append(write_textbox("<START_CAREER>", INDENT_SIZE, SPACING_SIZE*2))
    journal.button_bus.append(write_textbox("<CREDITS>", INDENT_SIZE, SPACING_SIZE*3))
    
    for button in journal.button_bus:
        if button.rect.collidepoint(offset_mouse):
            pygame.draw.rect(menu_canvas, (255,0,0), button.image.get_rect(topleft=(button.rect.x, button.rect.y)))
        button.draw(menu_canvas)
    
    for event in events:
        if event.type == MOUSEBUTTONDOWN:
            for button in journal.button_bus:
                if button.rect.collidepoint(offset_mouse):
                    if button == journal.button_bus[0]:
                        journal.gamestate = "DRAFT"
                        journal.seat_bus.append(Draft_Seat(0)) 
                        journal.hand_to_seat()
                        journal.seat_bus[0].update_hand_rects()
                    if button == journal.button_bus[2]:
                        journal.gamestate = "CREDITS"
                        journal.seat_bus.append(Draft_Seat(0)) 
                        journal.hand_to_seat()
                        journal.seat_bus[0].update_hand_rects()

    journal.button_bus = []
    return menu_canvas


def write_textbox(string, x, y):
    my_font = pygame.font.SysFont('Arial', 21)
    text_box = my_font.render(string, True, (0, 0, 0))
    return Widget(text_box, x, y)



##scenes 
##set object variables outside of scene, then change values in scene
def scene_credits(canvas, events, journal : Journal):
    canvas = pygame.Surface(MAX_WINDOW)
    canvas.fill((111,122,133))

    menu_canvas = journal.seat_bus[journal.active_seat].draft_menu.menu_interface(events, journal)
    canvas.blit(menu_canvas, (0,0))

    ##placehodler printing text box example
    write_textbox(f"hello world {journal.gamestate}", 0, 0).draw(canvas)
    write_textbox(f"gimpzillaYT", MAX_WINDOW[0]/2, MAX_WINDOW[1]/2).draw(canvas)

    
    return canvas
def scene_title(canvas, events, journal : Journal):
    canvas = pygame.Surface(MAX_WINDOW)
    canvas.fill((90,180,90))

    menu_canvas = menu_title(events, journal)
    canvas.blit(menu_canvas, (MAX_WINDOW[0]/2 - menu_canvas.get_width()/2, MAX_WINDOW[1]/2 - menu_canvas.get_height()/2))

    ##placehodler printing text box example
    write_textbox(f"hello world {journal.gamestate}", 0, 0).draw(canvas)

    
    return canvas

def scene_draft(canvas, events, journal : Journal):
    canvas = pygame.Surface(MAX_WINDOW)
    canvas.fill((90,180,90))
    active_seat = journal.seat_bus[journal.active_seat]
    
    field_ui = active_seat.draft_field.field_interface(events, journal)
    hand_ui = active_seat.hand_interface(events, journal)
    menu_ui = active_seat.draft_menu.menu_interface(events, journal)
    canvas.blit(hand_ui, (menu_ui.get_width(), MAX_WINDOW[1] - hand_ui.get_height()))
    canvas.blit(field_ui, (MAX_WINDOW[0]/4, 0))
    canvas.blit(menu_ui, (0, 0))

    if active_seat.is_active == True:
        canvas.blit(active_seat.active_card.image, journal.mouse_pos)

    ##placehodler printing text box example
    write_textbox(f"hello world {journal.gamestate}", 0, 0).draw(canvas)

    
    return canvas

##exe
asyncio.run(main())
