from PIL import Image


def add_shade(input_im, gradient=1.0, initial_opacity=1.0):
    if input_im.mode != 'RGBA':
        input_im = input_im.convert('RGBA')
    width, height = input_im.size

    alpha_gradient = Image.new('L', (width, 1), color=0xFF)
    for x in range(width):
        a = int((initial_opacity * 255.) * (1. - gradient * float(x) / width))
        if a > 0:
            alpha_gradient.putpixel((x, 0), a)
        else:
            alpha_gradient.putpixel((x, 0), 0)
    alpha = alpha_gradient.resize(input_im.size)

    black_im = Image.new('RGBA', (width, height), (255, 255, 255))
    black_im.putalpha(alpha)
    black_im = black_im.rotate(90)

    output_im = Image.alpha_composite(input_im, black_im)
    return output_im

if __name__ == "__main__":
    img = Image.new("RGBA", (500, 500), "#263238")
    img = add_shade(img, 1.0, 0.1)
    img.show()
