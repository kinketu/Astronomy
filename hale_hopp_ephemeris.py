import ephem

hb = ephem.readdb(
    'C/1995 O1 (Hale-Bopp),e,89.4245,282.4515,130.5641,183.6816,'
    '0.0003959,0.995026,0.1825,07/06.0/1998,2000,g -2.0,4.0'
    )

here = ephem.Observer()
here.lat, here.lon, here.elev = '33:45:10', '-84:23:37', 320.0

print "Hale-Bopp: date, right ascension, declination, and magnitude:"

here.date = ephem.date('1997/2/15')
end = ephem.date('1997/5/15')
while here.date < end:
    hb.compute(here)
    print here.date, hb.ra, hb.dec, hb.mag, ephem.constellation(hb)
    here.date += 5
