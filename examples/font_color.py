from itertools import cycle
from elektra import ElektraSearch

my_colors = ["#FFF59D", "#FFCC80", "#FFAB91", "#BCAAA4", "#EEEEEE"]

search = ElektraSearch()
search.add_words("python", "google", "harry", "potter", "accio")
search.set_grid_size((9, 9))
search.make_puzzle()

search.set_color_generator(cycle(my_colors))
# OR YOU CAN USE YOUR OWN GENERATOR!
search.set_font_size(40)
search.use_capital(True)
search.set_font_color("#263238")

search.render_photo()
search.print_solutions()
search.save_puzzle("font_color.jpg")
