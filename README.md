# reduce_gps_precision
Python command line tool to reduce GPS precision in EXIF data of JPEG images.

I use this to not disclose exactly where I live when I share images taken with
my phone on my blog. The algorithm simply sets the hundreths-of-minutes part of
the GPS coordinates to 0. This is not perfect (eg. what happens when that part
is already 0), but I can't think of an algorithm that is.
