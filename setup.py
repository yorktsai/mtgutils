try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'mtgutils',
    'author': 'York Tsai',
    'url': 'https://github.com/yorktsai/mtgutils',
    'version': '0.1',
    'install_requires': [
        "Pillow >= 3.0.0",
        "requests >= 2.8.1"
    ],
    'packages': ['mtgutils'],
    'scripts': [],
    'name': 'mtgutils'
}

setup(**config)
