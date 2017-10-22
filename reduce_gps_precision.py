#!/usr/local/bin/python

from PIL import Image
import piexif
import argparse

def reduce_gps_precision(path):
    try:
        exif_dict = piexif.load(path)
    except piexif._exceptions.InvalidImageDataError:
        return
    if 'GPS' not in exif_dict:
        return
    fixed = False
    if 'GPS' in exif_dict and len(exif_dict['GPS']):
        for key, value in exif_dict['GPS'].iteritems():
            try:
                if len(value) == 3 and len(value[2]) == 2 and value[2][0] and \
                        value[2][1] == 100:
                    exif_dict['GPS'][key] = (value[0], value[1], (0, 100))
                    fixed = True
            except TypeError:
                pass
    if fixed:
        print "Updating", path, "..."
        print exif_dict['GPS']
        exif_bytes = piexif.dump(exif_dict)
        im = Image.open(path)
        im.save(path, exif=exif_bytes)

def main():
    parser = argparse.ArgumentParser(
            description='Reduce precision of location data in an image.')
    parser.add_argument('path', nargs='+')

    args = parser.parse_args()
    for path in args.path:
        reduce_gps_precision(path)

if __name__ == '__main__':
    import sys
    sys.exit(main())
