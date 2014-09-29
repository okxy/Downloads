import urllib.request as ur
import re
import time
import random
import os

url = r'http://learnpythonthehardway.org/book'
urlx = r'http://learnpythonthehardway.org/book/appendixa.html'

with ur.urlopen(urlx) as web:
    html = web.read().decode('utf-8')
    
urls = re.findall(r'<li><a class="reference external" href="(.*?)">(.*?)</a></li>', html) + [('','')]


print(urls)

#<img alt="_static/python/win_notepadpp_ex1.png"
#images = re.findall(r"<img src='images/(.*?)'", html)

def makedir(x):
    try:
        os.mkdir(x)
    except:
        #print(x)
        makedir(os.path.dirname(x))
        makedir(x)

def download():
    
    for page, name in urls:
        urli = url + '//' + page
        #print(urli)
        time.sleep(random.randint(1,6))
        print(urli)
        
        with ur.urlopen(urli) as webi:
            htmlib = webi.read()  # once up        
            #fname = name.replace(':', ' - ').replace('?','').replace('!','') + r'.html'
            
            fname = page if page.endswith('html') else 'index.html'
            print(fname)
            if not os.path.exists(fname):
                try:                
                    with open(fname, 'wb') as f:
                        f.write(htmlib)
                except:
                    makedir(fname)
                    with open(fname, 'wb') as f:
                        f.write(htmlib)
                    print('created', fname)
                    
            print(name, 'written')
            htmli = htmlib.decode('utf-8')        
            images = [k for i,k in re.findall(r'<img(.*?)src="(.*?)"', htmli) + re.findall(r"<img(.*?)src='(.*?)'", htmli)]
            print(images)
            for im in images:
                
                image = urli = url + '/' + im
                print(image)
                if not os.path.exists(im):
                    
                    time.sleep(random.randint(1,6))
                    try:
                        ur.urlretrieve(image, im)
                        print(image, 'written')
                    except:
                        makedir(os.path.dirname(im))
                        ur.urlretrieve(image, im)
                        print(image, 'written with folder created')
                    finally:                        
                        pass
            
            css = re.findall(r'<link href="(.*?)" rel="stylesheet">', htmli) + re.findall(r"<link href='(.*?)' rel='stylesheet'>", htmli)
            print(images)
            for cs in css:             
                cssi = url + '/' + cs
                print(cssi)
                if not os.path.exists(cs):
                    time.sleep(random.randint(1,6))
                    try:
                        ur.urlretrieve(cssi, cs)
                        print(cs, 'written')
                    except:
                        makedir(os.path.dirname(cs))
                        ur.urlretrieve(cssi, cs)
                        print(cs, 'written with folder created')
                    finally:
                        pass
                    
            jss = re.findall(r'<script src="./(.*?)"></script>', htmli)
            print(jss)
            for js in jss:
                jsi = url + '/' + js
                print(jsi)
                if not os.path.exists(js):
                    time.sleep(random.randint(1,6))
                    try:
                        ur.urlretrieve(jsi, js)
                        print(js, 'written')
                    except:
                        makedir(os.path.dirname(js))
                        ur.urlretrieve(jsi, js)
                        print(js, 'written with folder created')
                    finally:
                        pass

    print()
    print('Congrats! It\'s finished.')

download()

def edit():
    import os
    files = os.listdir(os.getcwd())
    for f in files:
        if f.endswith('html'):
            with open(f,'rb+') as fi:           
                fi.write(fi.read().decode('utf-8').replace(r"<a href='/book/index.htmlindex.html'>", r"<a href='/index.html'>").encode('utf-8'))            
                print(f, 'updated')
#edit()
