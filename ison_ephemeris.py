import ephem

ison = ephem.readdb(
    'ISON,e,62.4042,295.6513,345.5377,12285,'
    '0.0000007,0.99999899,0.0000,11/28.7800/2013,2000,g 8.5,3.2',
    )

here = ephem.Observer()
here.lat, here.lon, here.elev = '33:45:10', '-84:23:37', 320.0

print "ISON: date, right ascension, declination, and magnitude:"

here.date = ephem.date('2013/9/1')
end = ephem.date('2013/12/1')
while here.date < end:
    ison.compute(here)
    print here.date, ison.ra, ison.dec, ison.mag, \
        ephem.constellation(ison)[1]
    here.date += 5
