# Simbad
from astroquery.simbad import Simbad
import astropy.coordinates as coord
import astropy.units as u

# set the timeout to 60s
# Simbad.TIMEOUT = 60

def test1():
    result_table = Simbad.query_object("m1")
    result_table.pprint(show_unit=True)

def test2():
    c = coord.ICRS("05h35m17.3s -05h23m28s")
    r = 5 * u.arcminute
    result_table = Simbad.query_region(c, radius=r)
    result_table.pprint(show_unit=True)

def test3():
    result_table = Simbad.query_object("m [1-9]", wildcard=True)
    print(result_table)
    print("\n")

def test4():
    result_table = Simbad.query_region("m81")
    print(result_table)

def test5():
    result_table = Simbad.query_region("m81", radius=0.1*u.deg)
    print(result_table)

def test6():
    # timeout
    result_table = Simbad.query_catalog('eso')
    print(result_table)

if __name__ == '__main__':
    test6()
