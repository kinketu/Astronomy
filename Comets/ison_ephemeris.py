from comet_ephemeris import comet_ephemeris

text = "C/2012 S1 (ISON),e,62.4042,295.6513,345.5377,12285," + \
    "0.0000007,0.99999899,0.0000,11/28.7800/2013,2000,g  8.5,3.2"
comet_ephemeris(text, "2013/9/1", "2013/12/1")
