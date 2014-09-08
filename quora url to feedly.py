#Python 3.3.5 (v3.3.5:62cf4e77f785, Mar  9 2014, 10:37:12) [MSC v.1600 32 bit (Intel)] on win32

# XML protocol: http://www.w3schools.com/xml/xml_validator.asp
"""
<?xml version="1.0" encoding="UTF-8"?>
<opml version="1.0">
 <head>
  <title>Choice Co subscriptions in Aol Reader</title>
 </head>
 <body>
  <outline title="绉戝銇湀" text="绉戝銇湀">
   <outline title="HHMI's Holiday Lectures o..." text="HHMI's Holiday Lectures o..." type="rss" xmlUrl="http://www.hhmi.org/biointeractive/HHMI_Lectures.xml" htmlUrl="http://www.hhmi.org/biointeractive/"/
   <...>
  </outline>
 </body>
</opml
"""

quora = r'https://www.quora.com/What-are-the-best-programming-blogs'

import os
import urllib.request as ur
import re


feedly = 'feedly.opml'

with open(feedly, 'rb') as f:  # ValueError: binary mode doesn't take an encoding argument
    content = f.read().decode('utf-8')
#contents = f.readlines()  # ValueError: I/O operation on closed file.

with open(feedly, 'rb') as f:
    contents = f.readlines()

for i in contents[:10]:
    print(i)
	
b'<?xml version="1.0" encoding="UTF-8"?>\n'
b'\n'
b'<opml version="1.0">\n'
b'    <head>\n'
b'        <title>Ch subscriptions in feedly Cloud</title>\n'
b'    </head>\n'
b'    <body>\n'
b'        <outline text="Seriously" title="Seriously">\n'
b'            <outline type="rss" text="The Glowing Python" title="The Glowing Python" xmlUrl="http://glowingpython.blogspot.com/feeds/posts/default?alt=rss" htmlUrl="http://glowingpython.blogspot.com/"/>\n'
b'            <outline type="rss" text="boredomandlaziness" title="boredomandlaziness" xmlUrl="http://www.boredomandlaziness.org/rss.xml" htmlUrl="http://www.curiousefficiency.org"/>\n'

for i in contents[-10:]:
    print(i)

	
b'        </outline>\n'
b'        <outline type="rss" text="Adrian Cockcroft\'s Blog" title="Adrian Cockcroft\'s Blog" xmlUrl="http://perfcap.blogspot.com/feeds/posts/default" htmlUrl="http://perfcap.blogspot.com/"/>\n'
b'        <outline type="rss" text="Code as Craft" title="Code as Craft" xmlUrl="http://codeascraft.etsy.com/feed/" htmlUrl="http://codeascraft.com"/>\n'
b'        <outline type="rss" text="phpied.com" title="phpied.com" xmlUrl="http://www.phpied.com/feed/" htmlUrl="http://www.phpied.com"/>\n'
b'        <outline type="rss" text="Subbu Allamaraju" title="Subbu Allamaraju" xmlUrl="http://feeds.feedburner.com/SubbuDotOrg" htmlUrl="http://www.subbu.org"/>\n'
b'        <outline type="rss" text="phly, boy, phly Atom Feed" title="phly, boy, phly Atom Feed" xmlUrl="https://mwop.net/blog/atom.xml" htmlUrl="http://mwop.net/blog"/>\n'
b'        <outline type="rss" text="Catchpoint\'s Blog" title="Catchpoint\'s Blog" xmlUrl="http://blog.catchpoint.com/feed/" htmlUrl="http://blog.catchpoint.com"/>\n'
b'        <outline type="rss" text="let us c new tech.. - Atom" title="let us c new tech.. - Atom" xmlUrl="http://tech2cp.blogspot.com/feeds/posts/default" htmlUrl="http://tech2cp.blogspot.com/"/>\n'
b'    </body>\n'
b'</opml>\n'

## with open(os.path.dirname + r'\new.opml', 'wb') as f:   # TypeError: unsupported operand type(s) for +: 'function' and 'str'


"""a href="http://www.xaprb.com/blog/" rel="nofollow" class="external_link" target="_blank" onmouseover="return require(&quot;qtext&quot;).tooltip(this, &quot;xaprb.com&quot;)">Xaprb</a></span><br /></li><li><span class="qlink_container"><a href="http://blog.zawodny.com/" rel="nofollow" class="external_link" target="_blank" onmouseover="return require(&quot;qtext&quot;).tooltip(this, &quot;zawodny.com&quot;)">Jeremy Zawodny&#039;s blog</a></span>"""

with ur.urlopen(quora) as f:
    html = f.read().decode('utf-8')

len(html)  # 228282
x = re.findall(r'a href="(.*?)" rel="nofollow" class="external_link" target="_blank" onmouseover="return require\(&quot;qtext&quot;\).tooltip\(this, &quot;(.*?)&quot;\)">(.*?)</a></span>', html)  # \ to escape（）
len(x)  # 141
xs = [(url, title.replace(r'&#039;', "'")) for url, title_com, title in x]
xs[:3]

from bs4 import BeautifulSoup as bs
soup = bs(html)
a = soup.find_all('a')
len(a)  # 380
exclude = ['gif', 'png', 'jpeg', 'css']
me = [re.findall(r'a href="(.*?)" rel="nofollow" class="external_link" target="_blank" onmouseover="return require\(&quot;qtext&quot;\).tooltip\(this, &quot;(.*?)&quot;\)">(.*?)</a></span>', i) or '' for i in a]  # TypeError: expected string or buffer
a[0]  # <a href="#" id="__w2_p1C7CWh_resume">Refresh this page</a>
for i in a:
    x = re.findall(r'a href="(.*?)" rel="nofollow" class="external_link" target="_blank" onmouseover="return require\(&quot;qtext&quot;\).tooltip\(this, &quot;(.*?)&quot;\)">(.*?)</a></span>', str(i))
    if x:
        me.append(x)

len(me)  # 0
me = [re.findall(r'a href="(.*?)" rel="nofollow" class="external_link" target="_blank" onmouseover="return require\(&quot;qtext&quot;\).tooltip\(this, &quot;(.*?)&quot;\)">(.*?)</a>', str(i))  for i in a]
len(me)  # 380
if '' in me:
	me.remove('')
len(me)  # 380
me[2]  # []
if [] in me:
    me.remove([])
len(me)  # 379

while [] in me:
    me.remove([])
len(me)  # 0
xs[:4]
len(xs)  # 141
xss = filter(lambda i: len(i[0]) < 100, xs)
##len(xss)  # TypeError: object of type 'filter' has no len()
len(list(xss))  # 105

xsl = list(xss)
xsl[:5]  # []

xm = [i for i in xs if len(i[0]) < 100]
len(xm)  # 105
xm[0]  # ('http://codeascraft.com/', 'Code as Craft')
xm[:6]  # [('http://codeascraft.com/', 'Code as Craft'), ('http://www.phpied.com/', "Stoyan's web dev blog: phpied.com"), ('http://www.subbu.org/', 'subbu.org - Subbu Allamaraju’s Blog'), ('http://mwop.net/blog.html', 'Blog Entries :: phly, boy, phly'), ('http://blog.catchpoint.com/', 'Web Performance Monitoring and Optimization'), ('http://www.sergeychernyshev.com/blog/', "Sergey Chernyshev's blog about projects and web in general.")]

########################              TODO                  #####################
# list all possible transformation from htmlurl to xmlurl
# then try the right one, except to continue
def com(text, url):        
	"http://codeascraft.etsy.com/feed/"
	"http://blog.catchpoint.com/feed/"
	"http://tech2cp.blogspot.com/feeds/posts/default"
	"https://mwop.net/blog/atom.xml"
	if r'blogspot.com' in url:
		urlfeed = url + r"/feeds/posts/default"
	else:
		urlfeed = url.rstrip(r'/') + r'/feed/'

		try:
			ur.urlopen(urlfeed, timeout=2)
		except:
			urlfeed = url + r"/atom.xml"

	return '        <outline type="rss" text="' + text + '" title="' + text + '" xmlUrl="' + urlfeed + '" htmlUrl="' + url +r'"/>' + '\n'  # r'\n' != '\n'

assert com(r"Catchpoint's Blog", r'http://blog.catchpoint.com') == r'        <outline type="rss" text="Catchpoint\'s Blog" title="Catchpoint\'s Blog" xmlUrl="http://blog.catchpoint.com/feed/" htmlUrl="http://blog.catchpoint.com"/>\n'
assert com(r"let us c new tech.. - Atom", r'http://tech2cp.blogspot.com/') ==  r'        <outline type="rss" text="let us c new tech.. - Atom" title="let us c new tech.. - Atom" xmlUrl="http://tech2cp.blogspot.com/feeds/posts/default" htmlUrl="http://tech2cp.blogspot.com/"/>\n'
        


with open(os.path.dirname(feedly) + r'\new.opml', 'wb') as f:  # TypeError: unsupported operand type(s) for +: 'function' and 'str'
    head = b"""<?xml version="1.0" encoding="UTF-8"?>\n\n<opml version="1.0">\n    <head>\n        <title>Ch subscriptions in feedly Cloud</title>\n    </head>\n    <body>\n        <outline text="Seriously" title="Seriously">\n"""
    end = b"""  </outline> </body>\n</opml>\n"""
    f.write(head)
    for url, title in xm:
        f.write(com(title.replace('&quot;',' ').replace(' &amp; ', ' & ').replace('  ', ' '), url).encode('utf-8'))  # AttributeError: 'str' object has no attribute 'encoding'       
    f.write(end)
with open(os.path.dirname(feedly) + r'\new.opml', 'rb') as f:
    htmlx = f.read()
    print(htmlx)


