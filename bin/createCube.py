from mtgutils import ImageFetcher
from mtgutils import Typesetter
import sys

if len(sys.argv) <= 1:
    print("%s <list file> <output dir>" % __file__)
    sys.exit()

list_file = sys.argv[1]
output_dir = sys.argv[2]

# build card list
cards = []
f = open(list_file, "r")
for line in f:
    line = line.strip()
    if len(line) <= 0:
        continue

    card = [line, 1]
    cards.append(card)

f.close()

# publish
typesetter = Typesetter(ImageFetcher())
typesetter.typeset(cards, output_dir)
