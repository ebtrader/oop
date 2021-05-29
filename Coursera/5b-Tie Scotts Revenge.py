# Scott's Revenge

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def draw(canvas):
    x, y = 200, 200
    w, h = 30, 150
    A = (x - w / 4, y - h / 2)
    B = (x + w / 4, y - h / 2)
    C = (x + w / 8, y - 3 * (h / 8))
    D = (x - w / 8, y - 3 * (h / 8))
    E = (x - w / 2, y + h / 4)
    F = (x, y + h / 2)
    G = (x + w / 2, y + h / 4)
    canvas.draw_polygon([A, B, C, D], 2, "Yellow", "Purple") # 7 width, red outline, white fill
    canvas.draw_polygon([C, D, E, F, G], 2, "Yellow", "Purple")

# create frame, labels and buttons
frame = simplegui.create_frame("Home", 400, 400)
frame.set_draw_handler(draw)

# start
frame.start()


