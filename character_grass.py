from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 100
y = 90
o = 1

while ( o > 0):
    while (x < 700):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x+2
        delay(0.01)
        
    while ( y < 500):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
            
    while (x > 100):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x-2
        delay(0.01)
        
    while ( y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y-2
        delay(0.01)

    while (x < 350):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x+2
        delay(0.01)

    r = 0


    while (r < 360):
        ssin = math.sin(r / 360 * 2 * math.pi)
        ccos = math.cos(r / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(ccos*200 + 350, ssin*200 + 300 )
        r = r+2
        delay(0.01)


    
close_canvas()
