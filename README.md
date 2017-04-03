# elektra
A beautiful, powerful, visual word search maker created with the power of Python!

## What exactly is a word search?
It is a kind of puzzle where you have to find words from. Why don't you check out this [Wikipedia page](https://en.wikipedia.org/wiki/Word_search)?

## Why use Elektra?
Right, you can simply use a word search generator websites. But do take a look at these:
* With Elektra, you can make a word search puzzle that looks waaaaaaaay better than other websites.
* It's written in Python! It uses Pillow, a fork of Python Imaging Library.
* It's really easy to use!
* It generates a PIL/Pillow Image object. So yes, you can edit it further, all you want!
* It's highly customizable. You can set your custom font, colors, grid size, box size etc! See the examples below.
* It's open source.

## Okay, but what are the things that I need?
* Python, obviously! Get Python 2.7.x from [here](https://www.python.org/downloads/).
* [Pillow](pillow.readthedocs.io/). It is a fork of PIL. You can install it by `pip install pillow --upgrade` if you have [pip](https://pypi.python.org/pypi/pip).

That's it!

## How do I install it?
Unfortunately, I still haven't packaged it yet. You have to clone this repository and write your scripts in the same directory that these files live in. For example:
* Run `git clone https://github.com/naeem-hasan/elektra` in the terminal or download and unzip this repository.
* Run `cd elektra` or manually go to that unzipped `elektra` folder.
* Write your script there so that you can `import elektra` with no problem.

## Alright, now I need to know how to create my puzzle.
Right. Consider this simple sample code:
```python
from elektra import ElektraSearch

search = ElektraSearch()
search.add_words("python", "google", "harry", "potter", "accio")
search.make_puzzle()
search.render_image()
search.save_image("simple.jpg")
```
This produces the following result:
![WORD_SEARCH](https://raw.githubusercontent.com/naeem-hasan/elektra/master/examples/simple.jpg)

## What are the other methods?
There, you're interested! An ElektraSearch object also has the following methods:
* `make_puzzle()` - Makes the word search puzzle.
* `render_image()` - Renders the image! Note that, before calling this method, you have to make the puzzle itself by calling the `make_puzzle()` method.
* `render_and_show()` - Basically, for debugging. It renders and immediately shows the output to screen.
* `get_image()` - Returns a PIL/Pillow Image object.
* `save_image(path, format=None)` - Saves the rendered image to `path`. Can also handle specified `format`.

For making the puzzle:
* `add_words(*args)` - Self explanatory. Use multiple arguments, if you want to use a list, don't forget to put an asterisk sign like this `search.add_words(*mylist)`.
* `set_grid_size(size)` - Specify the grid size by providing it a two number tuple like (x, y).
* `set_difficulty(difficulty)` - Set your puzzle difficulty with it! Use a number from 0 to 5.
  * 0 - Right
  * 1 - Right, down
  * 2 - Right, down, with right-down diagonals
  * 3 - Right, down, up, with right diagonals
  * 4 - All directions, with right diagonals
  * 5 - All directions, with all diagonals

Note that, the default difficulty level is 2. You can simply specify it when you're making the object too!

And the following methods are for visual customization:
* `use_shade(b)` - Whether the boxes should have white shades. Put a boolean variable here. This is turned on by default.
* `use_border(b)` - Whether the cells should be bordered. This is turned off by default. You can set the border width by calling `set_border_width(x)` method. The default with is set to 1.
* `set_border_color(x)` - Specify the border color here. Default is black. You can use a (R, G, B) tuple, or a hex string, or even a 'red' kind of string.
* `set_box_size(size)` - Takes a (x, y) tuple. You can set the cell size here. Default is (80, 80).
* `set_font_path(path)`, `set_font_size(x)`, `set_font_color(x)` - These are the methods for customizing fonts and text style.
* `set_color_generator(generator)` - Pass on your color generator function if you wish. It uses a random color generator by default.

## Show me some puzzles made with Elektra.
Sure!

![custom_border](https://raw.githubusercontent.com/naeem-hasan/elektra/master/examples/with_border.jpg)

![custom_color](https://raw.githubusercontent.com/naeem-hasan/elektra/master/examples/colors.jpg)

![custom_font_color](https://raw.githubusercontent.com/naeem-hasan/elektra/master/examples/font_color.jpg)
You can find all of these puzzles' codes in the examples folder!

I'd love if you contributed!
