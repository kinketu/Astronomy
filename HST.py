import math
import time
from datetime import datetime
import ephem
 
degrees_per_radian = 180.0 / math.pi
 
home = ephem.Observer()
# Tokyo
home.lon = '139.581'
home.lat = '35.6149'
home.elevation = 500
 
# Always get the latest hst TLE data from:
# http://www.celestrak.com/NORAD/elements/science.txt
hst = ephem.readtle('HST',
    '1 20580U 90037B   13361.70928184  .00002198  00000-0  14149-3 0  4040',
    '2 20580  28.4712  83.5513 0002750 254.3981 239.4568 15.04420296 98863'
)
 
while True:
    home.date = datetime.utcnow()
    hst.compute(home)
    print('hst: altitude %4.1f deg, azimuth %5.1f deg' % (hst.alt * degrees_per_radian, hst.az * degrees_per_radian))
    time.sleep(1.0)
