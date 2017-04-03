from itertools import cycle
from elektra import ElektraSearch

my_colors = ["#b71c1c", "#880E4F", "#4A148C"]

search = ElektraSearch()
search.add_words("python", "google", "harry", "potter", "accio")
search.set_grid_size((10, 10))
search.make_puzzle()

search.set_color_generator(cycle(my_colors))
# OR YOU CAN USE YOUR OWN GENERATOR!
search.set_font_size(40)
search.use_shade(False)
search.use_border(True)
search.use_capital(True)

search.render_photo()
search.print_solutions()
search.save_puzzle("colors.jpg")
