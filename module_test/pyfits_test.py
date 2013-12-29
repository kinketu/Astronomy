import pyfits
import numpy as np

n = np.arange(100.0)
hdu = pyfits.PrimaryHDU(n)
hdulist = pyfits.HDUList([hdu])
hdulist.writeto('./FITS_data/new.fits')

a1 = np.array(['NGC1001', 'NGC1002', 'NGC1003'])
a2 = np.array([11.1, 12.3, 15.2])
col1 = pyfits.Column(name='target', format='20A', array=a1)
col2 = pyfits.Column(name='V_mag', format='E', array=a2)
cols = pyfits.ColDefs([col1, col2])
tbhdu = pyfits.new_table(cols)

prihdr = pyfits.Header()
prihdr['COMMENT'] = "Here's some commentary about this FITS file."
prihdu = pyfits.PrimaryHDU(header=prihdr)

thdulist = pyfits.HDUList([prihdu, tbhdu])
thdulist.writeto('./FITS_data/table.fits')

hdulist.append(tbhdu)
hdulist.writeto('./FITS_data/image_and_table.fits')
