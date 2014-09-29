# Download Cell Snapshots (http://snapshots.cell.com/)
# by okxy(https://github.com/okxy) 2014-7-29
import urllib.request as ur
import time
import random
import os
import re

data_url = 'http://download.cell.com/images/edimages/Cell/snapshots/data.js'
with ur.urlopen(r'http://download.cell.com/images/edimages/Cell/snapshots/data.js') as html:
    s = html.read().decode('utf-8').replace('\n','')
    data = eval(s[s.find('['):s.rfind(']')+1])
    # print(data[:10])

files = os.listdir()
print(files)
success = failed = exist = 0
for i in data:
    title = i['title'].strip() + r'.pdf'  # well, automatically discarded by os
    url = re.sub('<.*?>', '', i['pdf']).translate(str.maketrans(':/','_-')) + r'?intermediate=true'
    
    if not title in files:
        try:
            ur.urlretrieve(url, title)
            success += 1
            print(title,'downloaded')
            time.sleep(random.randint(3,10))
        except:
            failed += 1
            print(title, 'FAILED.')  # to make it easily distinguishable
    else:
        exist += 1
        continue
    
else: print('finished.', str(success), 'downloaded', str(failed), 'failed', str(exist), 'already exist.')
 


	
