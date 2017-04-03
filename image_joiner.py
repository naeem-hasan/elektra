from PIL import Image


class ImageJoiner(object):
    def __init__(self, *args):
        self.images = []
        self._add_images(args)
        self.orientation = "horizontal"

    def add_image(self, image):
        self._add_images([image])

    def set_orientation(self, orientation):
        if orientation not in ["horizontal", "vertical"]:
            raise Exception("Invalid orientation! Use horizontal or vertical!")
        else:
            self.orientation = orientation

    def _add_images(self, images):
        for x in images:
            if isinstance(x, Image.Image):
                self.images.append(x)
            elif isinstance(x, str):
                self.images.append(Image.open(x))
            else:
                raise Exception("Invalid image! Use image paths or Image objects!")

    def _check_equal(self, lst):
        return len(set(lst)) <= 1

    def get_image(self):
        offset = 0
        if self.orientation == 'vertical':
            output_x = sum([i.size[0] for i in self.images])
            output_y = max([i.size[1] for i in self.images])
            I = 0
        else:
            output_x = max([i.size[0] for i in self.images])
            output_y = sum([i.size[1] for i in self.images])
            I = 1

        output = Image.new("RGBA", (output_x, output_y))

        for image in self.images:
            if self.orientation == "vertical":
                box = (offset, 0)
            else:
                box = (0, offset)
            output.paste(image, box)
            offset += image.size[I]

        return output
