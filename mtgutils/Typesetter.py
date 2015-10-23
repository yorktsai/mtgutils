from mtgutils import ImageFetcher
import os
from PIL import Image

class Typesetter:
    def __init__(self,
                 image_fetcher: ImageFetcher):
        self._image_fetcher = image_fetcher

    def typeset(self, cards, output_dir_path):
        sample_image = self._image_fetcher.get_image_by_name(cards[0][0])
        width = sample_image.size[0]
        height = sample_image.size[1]

        canvas = None
        canvas_counter = 0
        name_counter = 0

        for card in cards:
            name = card[0]
            num = card[1]

            # get image and resize if needed
            im = self._image_fetcher.get_image_by_name(name)
            if im.size[0] != width or im.size[1] != height:
                im = im.resize((width, height))

            for i in range(0, num):
                # initialize canvas if needed
                if canvas == None:
                    canvas = Image.new('RGBA', (width*3, height*3))
                    canvas_counter = 0

                # paste to canvas
                canvas.paste(im, (width * (canvas_counter % 3), height * (canvas_counter // 3)))
                canvas_counter += 1

                # output if there are 9 images
                if canvas_counter == 9:
                    canvas.save(os.path.join(output_dir_path, str(name_counter) + '.png'), 'PNG')
                    name_counter += 1
                    canvas_counter = 0
                    canvas = None

        # output if there are remaining image on canvas
        if canvas_counter > 0:
            canvas.save(os.path.join(output_dir_path, str(name_counter) + '.png'), 'PNG')




