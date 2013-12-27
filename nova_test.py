from novas import compat as novas
from novas.compat import eph_manager
jd_start, jd_end, number = eph_manager.ephem_open()

jd_tt = novas.julian_date(2013, 12, 27, 6.0)
print jd_tt

def print_planet(planet_name, planet_num):
    # make_object(type, number, name, star)
    # type = 0;major planet, Pluto, Sun, or Moon
    # type = 1; minor planet
    # type = 2; object located outside the soloar system
    # number; Mercury = 1, ..., Pluto = 9, Sun = 10, Moon = 11
    print planet_name
    planet = novas.make_object(0, planet_num, planet_name, None)
    ra, dec, dis = novas.astro_planet(jd_tt, planet)
    print 'R.A. %d:%02f' % (ra, abs(ra) % 1. * 60.)
    print 'dec. %d:%02f' % (dec, abs(dec) % 1. * 60.)
    print 'distance %f AU' % (dis,)

# Where is mars located.
print_planet('Mars', 4)

print_planet('Mercury', 1)
print_planet('Pluto', 9)
print_planet('Sun', 10)
print_planet('Moon', 11)
