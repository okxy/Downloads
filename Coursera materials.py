# You may need to log in your Coursera account via your browser, for me, Chrome, 
# to use this simple but sufficient script to download files in pptx, pdf, txt, srt, and mp4 as named as on the site.

import urllib.request as ur
from bs4 import BeautifulSoup as bs
import os
import re

url = r'https://class.coursera.org/learning-001/lecture'  # change to your course

html = ur.urlopen(url)
content = html.read().decode('utf-8')

soup = bs(content)
links = [link.get('href') for link in soup.find_all('a')] 
mylinks = [i for i in links if i.endswith('pptx') or 'mp4' in i or i.endswith('srt') or i.endswith('txt') or i.endswith('pdf')]
print(len(mylinks), 'links') # 231

with open(r'd:\gc\Desktop\learn.html', 'wb') as f, ur.urlopen(r'https://class.coursera.org/learning-001/lecture') as html:
    f.write(html.read())

os.chdir(os.getcwd())  # download files to the current folder
print(os.getcwd())

titles = [i.strip().replace(':','-').replace('?', ' - ') for i in re.findall(r'"hidden">Subtitles \(text\) for (.*?)</div>', content)]
print(len(titles),'titles')

linkx = []

for i in mylinks:    
    if i.endswith('pdf') or i.endswith('pptx'):
        fname = os.path.basename(i)
        if not os.path.exists(fname):        
            ur.urlretrieve(i, fname)
            print(i, 'downloaded')
        else:
            print(i, 'already downloaded')
    else:
        linkx.append(i)  ###!!!  linkx.remove(i)

print(len(linkx), 'links')  #195

if len(titles)*3 == len(linkx):
    for i in range(len(linkx)//3):
        title = titles[i]        
        ur.urlretrieve(linkx[3*i], title + r'.txt')
        ur.urlretrieve(linkx[3*i+1], title + r'.srt')
        ur.urlretrieve(linkx[3*i+2], title + r'.mp4')
        print(i, title)
else:
    print('not match')
