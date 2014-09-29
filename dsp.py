# for downloading the great book
# http://www.dspguide.com/CH3.PDF #ch1 - ch34

'''
url is case sensitive
use time.sleep to avoid partial download. But WHY?
'''

import urllib.request
import time
#         http://www.dspguide.com/CH1.PDF
url0 = r'http://www.dspguide.com/'
##
##print(url)
##file_name = url.split(r'/')[-1] 
##print(file_name )

for i in range(1,35):
    file = 'CH' + str(i) + r'.PDF' 
    url = url0 + file
    print("downloading " + file + '  from ' + url, end = ' ')
    urllib.request.urlretrieve(url, file)
    print('Success!')
    time.sleep(2)
    
print(finished)
