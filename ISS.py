import math
import time
from datetime import datetime
import ephem
 
degrees_per_radian = 180.0 / math.pi
 
home = ephem.Observer()
"""
home.lon = '-122.63'   # +E
home.lat = '45.56'      # +N
home.elevation = 80 # meters
"""
home.lon = '139.581'
home.lat = '35.6149'
home.elevation = 500
 
# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
    '1 25544U 98067A   13361.63412986  .00016717  00000-0  10270-3 0  9011',
    '2 25544  51.6474 229.8666 0005333 317.2191  42.8544 15.50078866 24713'
)
 
while True:
    home.date = datetime.utcnow()
    iss.compute(home)
    print('iss: altitude %4.1f deg, azimuth %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
    time.sleep(1.0)
