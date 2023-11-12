#!/usr/bin/env python3

from BeautifulSoup import BeautifulSoup
import urllib
import urllib2

def fortune():

        a = "a"
        for i in a:
         try:

                url= 'http://your-url-here.com/quote.php'
                req = urllib2.Request(url, headers={'User-Agent' : "Goose Browser"})
                page = urllib2.urlopen( req )
                soup = BeautifulSoup(page.read())
                quote =  soup.find("option").contents
                return quote[0]
         except Exception as e:
                return('honk honk honk honk honk!?')
