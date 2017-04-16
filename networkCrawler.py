
import urllib2
from urllib2 import urlopen, URLError
import thread

base_url = 'http://www.teamliquid.net/replay/download.php?replay='
# html_content_text = ''
# try:
#     html_content_byte = urlopen(base_url).read()
#     html_content_text = str(html_content_byte)
# except URLError as e:
#     print(e)
#
# print(html_content_text)


startIndex = 2073
fileNumber = 500


def downloadData(threadIndex, startIndex, fileNumber):
    for index in range(startIndex, startIndex - fileNumber, -1):
        url = base_url + str(index)
        try:
            downloadedFile = urllib2.urlopen(url)
            filePath = 'data/' + str(index) + '.rep'
            with open(filePath,'wb') as output:
                output.write(downloadedFile.read())
                print('Thread ' + str(threadIndex)  + ': rep file ' + str(index) + ' has been downloaded!')
        except URLError as e:
            print('Thread ' + str(threadIndex)  +': rep file ' + str(index) + ' fails downloaded!')


for threadIndex in range(0, 10, 1):
    try:
        thread.start_new_thread(downloadData, (threadIndex, startIndex - 100 * threadIndex, 100,))
    except:
        print('Error: unable to start new thread ' + str(threadIndex))


while 1:
    pass

# mp3file = urllib.urlopen("http://www.teamliquid.net/replay/download.php?replay=2092")
# with open('test.rep','wb') as output:
#     output.write(mp3file.read())