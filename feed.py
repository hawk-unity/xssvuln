import feedparser
url2=("https://www.mgm.gov.tr/FTPDATA/analiz/sonSOA.xml")
hava=feedparser.parse(url2)
i=0
for x in hava.entries:
    i+=1
    print(i,".hava")
    print(x.GenelDurum)
    print(x.title)
