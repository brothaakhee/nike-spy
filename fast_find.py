from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    concurrent = int(sys.argv[3])
except:
    start = 1480000
    end = 1490000
    concurrent = 10000
print 'hitting urls {0} - {1} with {2} threads'.format(start, end, concurrent)

q=Queue(concurrent*2)

def doWork():
    while True:
        url=q.get()
        getStatus(url)
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = httplib.HTTPConnection(url.netloc)   
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        if res.status not in [200, 404, 410]:
            doSomethingWithResult(res.status, ourl, res.getheader('location'))
    except:
        doSomethingWithResult("error", ourl, "exception")

def doSomethingWithResult(status, url, location):
    keywords = ['masterpiece', 'diamond', 'tiffany']
    if location:
        if any(keyword.lower() in location for keyword in keywords):
            print status, url[-7:], location
    else:
        print status, url

def load_skip_urls():
    skip_file = open('skip_ids.txt', 'r')
    skip_ids = [line.rstrip('\n') for line in skip_file]
    skip_file.close()
    return skip_ids

skip_ids = load_skip_urls()
ignore_ids = [
    1483759,
    1483753,
    1483757,
    1483761,
    1483767,
    1483775,
    1483763,
    1483765,
    1483751,
    1484599,
]


for i in range(concurrent):
    t=Thread(target=doWork)
    t.daemon=True
    t.start()
print 'created {0} threads'.format(concurrent)

try:
    urlBase = "http://store.nike.com/us/en_us/pd/anything/pid-"
    for i in range(start, end):
        product_id = str(i).zfill(6)
        if int(product_id) not in ignore_ids:
            url = urlBase + product_id
            q.put(url.strip())
    print 'finished loading all urls in queue'
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
