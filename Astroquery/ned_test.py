from astroquery.ned import Ned
import astropy.units as u
import astropy.coordinates as coord

def test1():
    result_table = Ned.query_object("NGC 224")
    print(result_table)

def test2():
    result_table = Ned.query_region("3c 273", radius=0.05*u.deg)
    print(result_table)

def test3():
    result_table = Ned.query_region(coord.FK4(ra=56.38, dec=38.43,
        unit=(u.deg, u.deg)), radius=0.1 * u.deg, equinox='B1950.0')
    print(result_table)

def test4():
    images = Ned.get_images("m1")
    print images

def test5():
    image_list = Ned.get_image_list("m1")
    print image_list

def test6():
    spectra = Ned.get_spectra("3c 273")
    print spectra

if __name__ == '__main__':
    test6()
