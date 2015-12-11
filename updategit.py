import subprocess
from subprocess import call
from HTMLParser import HTMLParser
#call(["git","clone","https://github.com/nwams/string-webapp"])


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
    def handle_endtag(self, tag):
        print "End tag:", tag


f = open('string-webapp/templates/ledger.html','r+')
page = f.read()
parser = MyHTMLParser()
parser.feed(page)
tableindex = page.find('<tbody>')
before =  page[0:tableindex+8]
after = page[tableindex+9:]


addedcode = "<tr><td class=\"mdl-data-table__cell--non-numeric\">Dec 8, 2015 </td><td class=\"mdl-data-table__cell--non-numeric\">Payment to Murat </td><td>200</td><td>7800</td></tr>"


newpage = before + addedcode + after 
#print newpage
f.write(newpage)

