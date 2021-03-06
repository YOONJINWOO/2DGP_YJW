import game_framework
import main_state_test
from pico2d import *


name = "LoadState"
image = None
logo_time = 0.0

def enter():
    global image0
    image0 = load_image('screen/loading_floor.png')


def exit():
    global image0
    del(image0)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state_test)





def draw():
    clear_canvas()
    image0.draw(600,350)
    update_canvas()


def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(main_state_test)
    delay(0.01)
    logo_time += 0.01