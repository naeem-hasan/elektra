from elektra import ElektraSearch

search = ElektraSearch()
search.add_words("python", "google", "harry", "potter", "accio")
search.make_puzzle()

search.set_font_size(40)
search.use_shade(False)
search.use_border(True)
search.use_capital(True)
search.set_border_width(2)
search.set_border_color("#3E2C1A")

search.render_photo()
search.save_puzzle("with_border.jpg")
