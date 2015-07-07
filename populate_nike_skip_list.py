import multiprocessing
import httplib2
import time
import webbrowser

pippinId = "721754"

def check_urls(start, span, offset):
    print "start"
    keywords = ["Hazelnut", "Doernbecher", "Pippen"]
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
        url = urlBase + product_id
        status, response = http.request(url)
        response404 = response[four_o_four_begin:four_o_four_end].lower()
        response_title = response[title_begin:title_end].lower()

        if response404.find("four-o-four") != -1:
            pass
            #print "404 " + str(url)
        elif any(keyword.lower() in response_title for keyword in keywords):
            matched_urls.append(url)
            #print "match! " + url
        else:
            valid_urls.append(url)
            print url
            skip_file = open('skip_ids.txt', 'a')
            skip_file.write(str(product_id) + "\n")
            skip_file.close()

    for url in matched_urls:
        pass
        #webbrowser.open_new_tab(url);
        print "match! " + url

def load_skip_urls():
    skip_file = open('skip_ids.txt', 'r')
    skip_ids = [line.rstrip('\n') for line in skip_file]
    skip_file.close()
    return skip_ids

def clear_skip_urls():
    skip_file = open('skip_ids.txt', 'w')
    skip_file.write("")
    skip_file.close()
    
if __name__ == '__main__':
    jobs = []
    offset = 500000

    clear_skip_urls()

    for i in range(500):
        p = multiprocessing.Process(target=check_urls, args=(i, 1000, offset))
        jobs.append(p)
        p.start()
