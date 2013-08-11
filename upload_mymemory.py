#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import httplib
import time
import codecs

fh = codecs.open('biblical_dictionary_only_wordnet.csv', 'r', 'utf-8')
names = fh.readline() 
codes = fh.readline()

codes = codes.split(';')

conn = httplib.HTTPConnection('api.mymemory.translated.net')

while True:

    try:
        line = fh.readline()
    except StopIteration:
        print "finished!"
        break
        
    line = line.split(';')
    no = int(line[0])
    print "Starting upload for %s" %line[1]
    time.sleep(1)
    for i in range(1, len(line)):

        print "Starting source language %s" %codes[i]

        for j in range(1, len(line)):
            
            if i == j:
                continue

        
            source = line[i].strip().lower().encode('utf-8')
            target = line[j].strip().lower().encode('utf-8')
            sl = codes[i].strip().encode('utf-8')
            tl = codes[j].strip().encode('utf-8')

            if source == '' or target == '':
                continue

            print "ID: %d Source Language: %s Target Language: %s Source: %s Target: %s" %(no,sl,tl,source,target)
            # insert email address 
            conn.request("GET", "/set?seg=" + source + "&tra=" + target + "&langpair=" + sl + "|" + tl + "&de=XXX@gmail.com")
            response = conn.getresponse()
            if not response.status == 200:
                print >> sys.stderr, "Response from Server is: %s" %str(response.status) 
            
        
            
        
conn.close()
fh.close()
