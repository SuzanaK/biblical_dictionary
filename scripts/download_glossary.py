#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import urllib
import codecs
from bs4 import BeautifulSoup

""" Download article names and IDs of the Insight book from wol.jw.org and save both in a csv file. """

# must be changed according to target language!
url = 'http://wol.jw.org/nl/wol/d/r18/lp-o/'

# 'Abel'
start = 1200000005
# 'Zuzim'
end = 1200004774

out = codecs.open("glossary.csv", "w", "utf-8")

rows = ""
currentid = start
index = 0
counter = 0

while currentid <= end:
    
    currentid = start + index
    id = str(currentid)
    fh = urllib.urlopen(url + str(currentid))
    html = fh.read()
    soup = BeautifulSoup(html)
    
    p0 = soup.find(id="p0")
    if p0 == None:
        word = ">>None<<"
    else: 
        
        bold = p0.find("b")
        if bold == None:
            word = ">>None<<"
        else: 
            # the word we are looking for is the text in bold
            word = bold.get_text()
    # wait to avoid strain on the jw.org servers
    time.sleep(0.5)
    # each row in the csv file will consist of the ID and the word
    new_row = id + ";" + word + "\n"
    print(new_row)
    # force print on stdout
    sys.stdout.flush()
    rows += new_row
    # write into file all 100 lines
    counter += 1
    if counter % 100 == 0:
        out.write(rows)
        rows = ""
        counter = 0

    index += 1
    # Ende der while Schleife

# write the rest
out.write(rows)
# ...and close the file.
out.close()
