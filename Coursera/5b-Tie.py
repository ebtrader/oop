import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# images
#joe = simplegui.load_image("http://farm9.staticflickr.com/8560/8876956295_fa57030cf4_o.png")
img_sz = (171, 370)
img_ctr = (img_sz[0]//2, img_sz[1]//2)

class Tie:
    def __init__(self, color):
        self.color = color
        self.width = 50
        self.height = 100

    def __str__(self):
        return "I am a " + self.color + " tie."


tie1 = Tie("Blue")
tie2 = Tie("Red")

print(tie1)
print(tie2)






