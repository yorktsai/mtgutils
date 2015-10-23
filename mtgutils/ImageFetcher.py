import io
import os
from PIL import Image
import re
import requests
import time


class ImageFetcher:
    def __init__(self):
        # cache directory
        self._cache_dir_path = os.path.join(os.path.expanduser('~'), ".mtgutils_cache")
        if not os.path.exists(self._cache_dir_path):
            os.mkdir(self._cache_dir_path)

        self.btype_cache_dir_path = os.path.join(self._cache_dir_path, "btype")
        if not os.path.exists(self.btype_cache_dir_path):
            os.mkdir(self.btype_cache_dir_path)

    def get_images_by_name(self, name):
        rt = []

        # check cache file
        cache_filepath = os.path.join(self._cache_dir_path, name + ".jpg")
        if os.path.exists(cache_filepath):
            rt.append(Image.open(cache_filepath))

        # check b-type cache
        btype_filepath = os.path.join(self._cache_dir_path, "btype", name + ".jpg")
        if os.path.exists(btype_filepath):
            rt.append(Image.open(btype_filepath))

        if len(rt) > 0:
            return rt

        # search from http://magiccards.info/
        r = requests.get("http://magiccards.info/query", params={'q': name})
        print("fetching %s ..." % r.url)
        # use the first match
        m = re.search('(http://magiccards.info/scans/en/[0-9a-z]+/[0-9a-z]+)\.jpg', r.text)
        image_url = m.group(0)

        # fetch image
        r = requests.get(image_url)
        im = Image.open(io.BytesIO(r.content))

        # save it to cache
        im.save(cache_filepath, 'JPEG')

        # append to result
        rt.append(im)

        # check b-type
        if m.group(1).endswith("a"):
            # fetch image
            r = requests.get(m.group(1)[:-1] + "b.jpg")
            im = Image.open(io.BytesIO(r.content))

            # save it to cache
            im.save(btype_filepath, 'JPEG')

            # append to result
            rt.append(im)

        # fetch delay
        time.sleep(5)

        return rt
