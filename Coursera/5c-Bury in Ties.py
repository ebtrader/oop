# Scott's Revenge

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# images
joe = simplegui.load_image("http://farm9.staticflickr.com/8560/8876956295_fa57030cf4_o.png")
img_sz = (171, 370)
img_ctr = (img_sz[0] // 2, img_sz[1] // 2)

# globals
COLORS = ["Blue", "Red", "Yellow", "Green", "Maroon",
          "Aqua", "Fuchsia", "Lime", "Teal", "Olive",
          "Silver", "Purple"]
color_key = 0
ties = []


# classes
class Tie:
    def __init__(self):
        self.height = 150
        self.width = 30
        self.color = "White"
        self.location = (50, 200)

    def __str__(self):
        return "I am a " + self.color + " tie."

    def draw(self, canvas):
        x, y = self.location[0], self.location[1]
        w, h = self.width, self.height
        A = (x - w / 4, y - h / 2)
        B = (x + w / 4, y - h / 2)
        C = (x + w / 8, y - 3 * (h / 8))
        D = (x - w / 8, y - 3 * (h / 8))
        E = (x - w / 2, y + h / 4)
        F = (x, y + h / 2)
        G = (x + w / 2, y + h / 4)
        canvas.draw_polygon([A, B, C, D], 1, "Black", self.color)
        canvas.draw_polygon([C, D, E, F, G], 1, "Black", self.color)

    def change_color(self, color):
        self.color = color

    def drag(self, pos):
        self.location = pos


# event handlers
def drag(pos):
    ties[-1].drag(pos)


def new_tie():
    ties.append(Tie())


def new_color():
    global color_key
    color_key += 1
    color_key %= 12
    ties[-1].change_color(COLORS[color_key])


# draw handler
def draw(canvas):
    canvas.draw_image(joe, img_ctr, img_sz, (250, 215), img_sz)

    for tie in ties:
        tie.draw(canvas)


# create frame, labels and buttons
frame = simplegui.create_frame("Scott's Revenge", 400, 400)
frame.set_draw_handler(draw)
frame.set_mousedrag_handler(drag)
frame.add_button("Make New Tie", new_tie, 100)
frame.add_button("Change Color", new_color, 100)
frame.add_label("")
frame.add_label("Drag a tie onto Joe")
frame.add_label("")
frame.add_label("Or a hundred!!")

# start
frame.start()

