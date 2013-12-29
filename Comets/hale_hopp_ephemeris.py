from comet_ephemeris import comet_ephemeris

text = 'C/1995 O1 (Hale-Bopp),e,89.4245,282.4515,130.5641,183.6816,' + \
    '0.0003959,0.995026,0.1825,07/06.0/1998,2000,g -2.0,4.0'
comet_ephemeris(text, "1997/2/15", "1997/5/15") 
