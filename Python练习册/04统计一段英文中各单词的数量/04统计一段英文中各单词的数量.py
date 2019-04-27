import re
import os
from pprint import pprint
from collections import Counter
path = os.getcwd() + '/test.txt'


def wordstat(path):
    f = open(path, 'r+')
    words = f.read()
    l = re.split(r'[" ",.\n]',words)
    counter = Counter(l)

    pprint(counter.most_common())


if __name__ == '__main__':
	wordstat(path)