from elektra import ElektraSearch

search = ElektraSearch()
search.add_words("python", "google", "harry", "potter", "accio")
search.make_puzzle()
search.render_photo()
search.save_puzzle("simple.jpg")
