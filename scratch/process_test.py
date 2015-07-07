import multiprocessing
import time

def count_one_thousand(start, step):
    for i in range(start*step, start*step+step):
        f = open('parallel_count_output.txt', 'a')
        f.write(str(i) + "\n")
        f.close()
    return

def print_one():
    print "1"
    return

def count_one_million():
    start = time.clock()
    for i in range(100000):
        f = open('serial_count_output.txt', 'a')
        f.write(str(i) + "\n")
        f.close()

    stop = time.clock()
    print stop-start

if __name__ == '__main__':
    f = open('parallel_count_output.txt', 'w')
    f.write("")
    f.close()

    start = time.clock()

    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=count_one_thousand, args=(i,100000))
        jobs.append(p)
        p.start()

    stop = time.clock()
    print stop-start

    f = open('serial_count_output.txt', 'w')
    f.write("")
    f.close()

    count_one_million()
