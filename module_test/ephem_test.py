import ephem
mars = ephem.Mars()
mars.compute('2013/12/27')
print mars.ra, mars.dec
print mars.earth_distance

m = ephem.Mars('1970')
print ephem.constellation(m)

m = ephem.Mars('2003/8/27')
print m.name, m.elong, m.size

j = ephem.Jupiter()
j.compute('1986/2/8')
print j.ra, j.dec
j.compute('1986/2/9', epoch='1950')
print j.a_ra, j.a_dec

gatech = ephem.Observer()
gatech.lon = '-84.39733'
gatech.lat = '33.775867'
gatech.elevation = 320
gatech.date = '1984/5/30 16:22:56'
v = ephem.Venus(gatech)
print v.alt, v.az

m = ephem.Moon('1980/6/1')
print ephem.constellation(m)
print ephem.delta_t('1980')

ephem.julian_date('2000/1/1')

print ephem.previous_new_moon(ephem.now())
print ephem.next_new_moon(ephem.now())
# localtime
print ephem.localtime(ephem.next_new_moon(ephem.now()))

print ephem.previous_full_moon(ephem.now())
print ephem.next_full_moon(ephem.now())
# localtime
print ephem.localtime(ephem.next_full_moon(ephem.now()))

rigel = ephem.star('Rigel')
print rigel._ra, rigel._dec

# astronomical constants
print ephem.meters_per_au
print ephem.earth_radius
print ephem.moon_radius
print ephem.sun_radius
print ephem.c
