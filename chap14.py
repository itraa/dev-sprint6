# This is where chapter 14 exercises go.
import urllib
#from HTMLParser import HTMLParser

fout = open('output.txt', 'w')
param = raw_input("Enter zip code: ")
conn = urllib.urlopen("http://www.uszip.com/zip/%s" % param)
fout.write(conn.read())
fp = open('output.txt')
for line in fp:
    line = line.strip()
    if 'Population' in line:
        print line
fp.close()

#for line in conn:
#    line.strip()
