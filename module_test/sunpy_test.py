import sunpy
from sunpy.map import Map
import matplotlib.pyplot as plt

# quick plot
def test1():
    aia = Map(sunpy.AIA_171_IMAGE)
    aia.peek()

# plot
def test2():
    aia = Map(sunpy.AIA_171_IMAGE)
    fig = plt.figure()
    ax = plt.subplot(111)
    aia.plot()
    plt.colorbar()
    aia.draw_limb()
    plt.show()

def test3():
    from sunpy.sun import constants as con
    # one astronomical unit (the average distance between the sun ant Earth)
    print(con.au)
    # the solar radius
    print(con.radius)

if __name__ == '__main__':
    test3()
