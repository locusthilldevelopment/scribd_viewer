from bs4 import BeautifulSoup as BS4
from urlparse import urlparse
import urllib2
url = "http://d1.scribdassets.com/ScribdViewer.swf?document_id=()&access_key=$$$"
prompt = raw_input("Input document URL: ")
response = urllib2.urlopen(prompt)
html = response.read()
soup = BS4(html, 'html.parser')
#print(soup.prettify())
script = soup('script', {'type' : 'text/javascript'})
#print script
o = urlparse(prompt)
doc_id = filter(lambda x: x.isdigit(), prompt)
dict = script[6].contents[0]
dict = dict.replace("Scribd.ReadPage.early_initialize();", "")
dict = dict.replace("Scribd.current_doc = ", "")
dict = dict.replace(";Scribd.eligible_for_seo_roadblock = false;$(document).trigger('scribd:docinfo_ready');"
, "")
start =  dict.find("\"access_key\"")
end = start + 38
main = dict[start:end]
key = main.replace("\"access_key\":\"", "")
key = key.replace("\"", "")
url = url.replace("()", doc_id)
url = url.replace("$$$", key)
print "****"
print "OPEN IN BROWSER: \n"
print url
print "\n"
print "****"
