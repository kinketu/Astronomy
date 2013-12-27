from astroquery import fermi
from astropy.io import fits

result = fermi.FermiLAT.query_object('M31', energyrange_MeV='1000, 100000', obsdates='2013-01-01 00:00:00, 2013-01-02 00:00:00')
print result
sc = fits.open(result[0])
