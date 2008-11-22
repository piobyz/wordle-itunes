"""
Mac OS X only.
Returns all iTunes library artists with respect to number of albums.
Then copy & paste an output to http://www.wordle.net/create
"""

__author__ = "Piotr Byzia"
__license__ = "GPL"
__version__ = "0.1.0"
__email__ = "piotr.byzia@gmail.com"

import sys
import os

do_not_include = ['Movies', 'Podcasts', 'Compilations']

def dirListing(directory):
    """Returns a list of directories."""
    dirs = [] #list of directories

    #list of directories and files
    library = os.listdir(directory)

    for artist in library:
        if artist not in do_not_include:
            if os.path.isdir(directory + os.sep + artist):
                albums = os.listdir(directory + os.sep + artist)
                albums_no = 0
                for album in albums:
                    albums_no += 1
                # Add artists albums_no numbers of times so that wordle logo
                # can take in into account.
                for i in range(albums_no):
                    # Add handling of spaces in artist's names
                    dirs.append(artist.replace(' ', '~'))
    return dirs

def main():
    wordle_input = dirListing('/Users/%s/Music/iTunes/iTunes Music/' % os.environ['USER'])
    for i in range(len(wordle_input)):
        print('%s' % wordle_input[i])
    
if __name__ == '__main__':
    main()
