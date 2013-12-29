import ephem

def comet_ephemeris(text, start_date, end_date):
    comet = ephem.readdb(text)

    here = ephem.Observer()
    here.lat, here.lon, here.elev = '33:45:10', '-84:23:37', 320.0

    comet_name = text.split(",")[0]
    print comet_name + \
        ": date, right ascension, declination, and magnitude:"

    here.date = ephem.date(start_date)
    end = ephem.date(end_date)
    while here.date < end:
        comet.compute(here)
        print here.date, comet.ra, comet.dec, comet.mag, \
            ephem.constellation(comet)[1]
        here.date += 5

if __name__ == '__main__':
    text = 'C/2013 R1 (Lovejoy),e,64.0406,70.7108,67.1677,504.9223,' + \
        '0.0000869,0.99839219,0.0000,12/22.7340/2013,2000,g 10.0,4.0'
    comet_ephemeris(text, "2013/9/1", "2013/12/1")
