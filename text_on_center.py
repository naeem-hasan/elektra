from PIL import Image, ImageDraw, ImageFont

DEFAULT_FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
DEFAULT_FONT_SIZE = 50
DEFAULT_IMG_SIZE = (500, 500)
DEFAULT_BG_COLOR = (0, 0, 0)
DEFAULT_TEXT_COLOR = (255, 255, 255)


class TextOnCenter(object):
    def __init__(self, image=None, image_size=(-1, -1), font_path=DEFAULT_FONT_PATH, font_size=DEFAULT_FONT_SIZE, text_color=DEFAULT_TEXT_COLOR, bg_color=DEFAULT_BG_COLOR, text=""):
        if image is None:
            if image_size == (-1, -1):
                self.image_size = DEFAULT_IMG_SIZE
            else:
                self.image_size = image_size
            self.image = Image.new("RGB", self.image_size, color=bg_color)
        else:
            if image_size != (-1, -1):
                self.image = image.resize(image_size)
                self.image_size = image_size
            else:
                self.image = image
                self.image_size = image.size

        self.font = ImageFont.truetype(font_path, font_size)
        self.text = text
        self.draw = ImageDraw.Draw(self.image)
        self.text_color = text_color

    def set_text(self, text):
        self.text = text

    def draw_text(self):
        w, h = self.draw.textsize(self.text, self.font)
        if '\n' in self.text:
            self.draw.multiline_text(((self.image_size[0] - w) / 2, (self.image_size[1] - h) / 2), self.text, self.text_color, self.font, align="center")
        else:
            self.draw.text(((self.image_size[0] - w) / 2, (self.image_size[1] - h) / 2), self.text, self.text_color, self.font)

    def get_image(self):
        return self.image

    def show_image(self):
        self.image.show()
