import word_search
import image_joiner
import text_on_center
from PIL import Image, ImageOps
from random import choice
from add_shade import add_shade
from os.path import dirname, realpath, join


class ElektraSearch(object):
    COLORS = [(211, 47, 47), (198, 40, 40), (183, 28, 28), (194, 24, 91), (173, 20, 87), (136, 14, 79), (123, 31, 162), (106, 27, 154), (74, 20, 140), (81, 45, 168), (69, 39, 160), (49, 27, 146), (48, 63, 159), (40, 53, 147), (26, 35, 126), (13, 71, 161), (21, 101, 192), (25, 118, 210), (2, 119, 189), (1, 87, 155), (0, 96, 100), (0, 131, 143), (0, 105, 92), (0, 77, 64), (27, 94, 32), (46, 125, 50), (85, 139, 47), (51, 105, 30), (158, 157, 36), (130, 119, 23), (249, 168, 37), (245, 127, 23), (255, 143, 0), (255, 111, 0), (230, 81, 0), (239, 108, 0), (191, 54, 12), (216, 67, 21), (78, 52, 46), (62, 39, 35), (66, 66, 66), (33, 33, 33), (38, 50, 56)]
    DEFAULT_FONT = "FjallaOne-Regular.ttf"

    def __init__(self, words=[], grid_size=(8, 8), difficulty=2):
        self.words = set(words)
        self.grid_size = grid_size
        self.difficulty = difficulty

        self.is_shade = True
        self.is_border = False
        self.color_generator = self._random_color_gen
        self.border_width = 1
        self.border_color = (0, 0, 0)
        self.box_size = (80, 80)
        self.font_path = join(dirname(realpath(__file__)), ElektraSearch.DEFAULT_FONT)
        self.font_size = 28
        self.font_color = (255, 255, 255)
        self.iteration = 30
        self.is_capital = False

        self.is_rendered = False
        self.image = self._generate_blank()

        self.puzzle, self.solution = self._generate_search()

    def render_image(self):
        if callable(self.color_generator):
            colors = self.color_generator()
        else:
            colors = self.color_generator

        y_chunks = []
        for i in xrange(self.grid_size[1]):
            x_chunks = []
            for j in xrange(self.grid_size[0]):
                chunk = Image.new("RGBA", self.box_size, colors.next())
                if self.is_shade:
                    chunk = add_shade(chunk, gradient=1.0, initial_opacity=0.3)
                if self.is_border:
                    chunk = ImageOps.expand(chunk, border=self.border_width, fill=self.border_color)
                if self.is_capital:
                    let = self.puzzle[i][j].upper()
                else:
                    let = self.puzzle[i][j].lower()
                text_chunk = text_on_center.TextOnCenter(image=chunk, font_path=self.font_path, font_size=self.font_size, text_color=self.font_color, text=let)
                text_chunk.draw_text()
                chunk = text_chunk.get_image()
                x_chunks.append(chunk)

            joiner = image_joiner.ImageJoiner(*x_chunks)
            joiner.set_orientation("vertical")
            y_chunks.append(joiner.get_image())

        joiner = image_joiner.ImageJoiner(*y_chunks)
        if self.is_border:
            self.image = ImageOps.expand(joiner.get_image(), border=self.border_width, fill=self.border_color)
        else:
            self.image = joiner.get_image()
        self.is_rendered = True

    def render_and_show(self):
        self.render_image()
        self.get_image().show()

    def get_image(self):
        return self.image

    def get_solutions(self):
        return self.solution

    def print_solutions(self):
        for x in self.get_solutions():
            print "{}: {} {}".format(*x)

    def save_image(self, path, format=None):
        self.image.save(path, format)

    def make_puzzle(self):
        self.puzzle, self.solution = self._generate_search()

    def add_words(self, *args):
        self.words = self.words.union(set(args))

    def set_grid_size(self, size):
        self.grid_size = size

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def use_shade(self, b):
        self.is_shade = b

    def use_border(self, b):
        self.is_border = b

    def set_border_width(self, x):
        self.border_width = x

    def set_border_color(self, x):
        self.border_color = x

    def set_box_size(self, size):
        self.box_size = size

    def set_font_path(self, path):
        self.font_path = path

    def set_font_size(self, x):
        self.font_size = x

    def set_font_color(self, x):
        self.font_color = x

    def set_iterations(self, x):
        self.iteration = x

    def set_color_generator(self, generator):
        self.color_generator = generator

    def use_capital(self, b):
        self.is_capital = b

    def _make_grid(self, size):
        return [['x' for i in range(size[0])] for j in range(size[1])]

    def _generate_blank(self):
        blank = text_on_center.TextOnCenter(image_size=(500, 500), font_path=self.font_path, text_color=(80, 80, 80), bg_color=(180, 180, 180), text="Puzzle not yet rendered")
        blank.draw_text()
        return blank.get_image()

    def _random_color_gen(self):
        while True:
            yield choice(ElektraSearch.COLORS)

    def _generate_search(self):
        if not self.words:
            return self._make_grid(self.grid_size), [[]]

        search = word_search.WordSearch(*self.grid_size)
        search.difficulty(self.difficulty)
        search.generate(self.iteration, words=list(self.words))
        return search.display(), search.solutions()
