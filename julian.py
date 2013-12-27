import julianday
import ephem

jd = julianday.JD.from_calendar_datetime(2012, 4, 1, 0, 0, 0)
print jd.calendar_datetime()

tmp = ephem.julian_date('2012/4/1')
jd = julianday.JD(tmp)
print jd.calendar_datetime()
