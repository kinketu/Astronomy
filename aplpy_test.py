# ipython --pylab

import urllib2, tarfile
url = 'http://python4astronomers.github.com/_downloads/APLpy-example.tar'
tarfile.open(fileobj=urllib2.urlopen(url), mode='r|').extractall()
cd APLpy-example
ls

import aplpy
f = aplpy.FITSFigure('ngc2264_cutout.fits')
f.show_grayscale()
f.show_contour('ngc2264_cutout_mips.fits', levels=10)
f.add_scalebar(0.03, '0.5pc', color='white')
f.save('my_first_plot.eps')
