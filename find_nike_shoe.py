import multiprocessing
import httplib2
import time
import webbrowser
from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

pippinId = "721754"

def check_urls(skip_ids, start, span, offset):
    keywords = ["patriots",]
    title_begin = 500
    title_end = 1500
    urlBase = "http://store.nike.com/us/en_us/pd/anything/pid-"
    four_o_four_begin = 47800
    four_o_four_end = 48000
    valid_urls = []
    matched_urls = []

    http = httplib2.Http()

    for i in range(start*span+offset, start*span+span+offset):
        product_id = str(i).zfill(6)
        status, url, location = getStatus(urlBase + product_id)
        if status not in [404, 410]:
            doSomethingWithResult(status, url, location)
        #if product_id not in skip_ids:
        #    url = urlBase + product_id
        #    status, response = http.request(url)
        #    response404 = response[four_o_four_begin:four_o_four_end].lower()
        #    response_title = response[title_begin:title_end].lower()
    
        #    if response404.find("four-o-four") != -1:
        #        pass
        #        #print "404 " + str(url)
        #    elif any(keyword.lower() in response_title for keyword in keywords):
        #        matched_urls.append(url)
        #        print "match! " + url
        #    else:
        #        valid_urls.append(url)
    #for url in matched_urls:
        #webbrowser.open_new_tab(url);
        #print url

def doSomethingWithResult(status, url, location):
    keywords = ['pippen', 'hazelnut', 'patriots']
    if any(keyword.lower() in location for keyword in keywords):
        print status, url, location


def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = httplib.HTTPConnection(url.netloc)   
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl, res.getheader('location')
    except:
        return "error", ourl, "nothing"

def load_skip_urls():
    skip_file = open('skip_ids.txt', 'r')
    skip_ids = [line.rstrip('\n') for line in skip_file]
    skip_file.close()
    return skip_ids

if __name__ == '__main__':
    print "start"
    jobs = []
    offset = 900000
    skip_ids = load_skip_urls()
    processes = 5000
    print "spinning up {0} processes".format(processes)
    for i in range(processes):
        p = multiprocessing.Process(target=check_urls, args=(skip_ids, i, 20, offset))
        jobs.append(p)
        p.start()
