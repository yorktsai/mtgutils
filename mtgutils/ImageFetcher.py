import io
import os
from PIL import Image
import re
import requests
import time

class ImageFetcher:
    def __init__(self):
        # cache directory
        self._cacheDirPath = os.path.join(os.path.expanduser('~'), ".mtgutils_cache")
        if not os.path.exists(self._cacheDirPath):
            os.mkdir(self._cacheDirPath)

    def get_image_by_name(self, name):
        # check cache file
        cache_filepath = os.path.join(self._cacheDirPath, name + ".jpg")
        if os.path.exists(cache_filepath):
            return Image.open(cache_filepath)

        # search from http://magiccards.info/
        r = requests.get("http://magiccards.info/query", params={'q': name})
        m = re.search('http://magiccards.info/scans/en/[0-9a-z]+/[0-9]+\.jpg', r.text)
        image_url = m.group(0)  # use the first match

        # fetch image
        r = requests.get(image_url)
        im = Image.open(io.BytesIO(r.content))

        # save it to cache
        im.save(cache_filepath, 'JPEG')

        # fetch delay
        time.sleep(1)

        return im
