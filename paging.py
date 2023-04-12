# Yudhvir Sirkissoon
# srkyud001

import sys
import random
pages = ""

for i in range(10):
    r = random.randint(0,9)
    pages = pages + str(r)

#pages = "7012030423030321201701"
#pages = "121030424"
#pages="70120304230323"
print(pages)

def FIFO(size, pages):
    queue = []
    miss=0 
    hit=0
    oldest_pos=0
    for i in pages:
        if oldest_pos == size:
            oldest_pos = 0
        if len(queue)<size and i not in queue:
            queue.append(i)
            miss +=1
        elif len(queue) == size and i not in queue:
            queue[oldest_pos] = i
            oldest_pos = oldest_pos+1
            miss +=1
        else:
            hit+=1
    return miss

def LRU(size, pages):
    queue = []
    miss=0 
    hit=0
    for i in pages:
        if len(queue)<size and i not in queue:
            queue.append(i)
            miss +=1
        elif len(queue) == size and i not in queue:
            # queue[0] is always the least recently used
            queue.remove(queue[0])
            queue.append(i)
            miss +=1
        else:
            # this is the essence of the algorithm, since the i has been used,
            # it moves to the end on the queue, keeping the lru in the first pos
            queue.remove(i)
            queue.append(i)
            hit+=1
    return miss

def OPT(size, pages):
    def get_longest_distance(queue, other):
        ld = 0
        p=0
        for i in range(len(queue)):
            pos = other.find(queue[i])
            if pos ==-1:
                return i
            if pos!=-1 and pos>ld:
                p=i
                ld = pos
        return p
        
    queue = []
    miss=0 
    hit=0

    for i in range(len(pages)):
        if len(queue)<size and pages[i] not in queue:
            queue.append(pages[i])
            miss +=1
        elif len(queue) == size and pages[i] not in queue:
            p = get_longest_distance(queue, pages[i::])
            queue[int(p)] = pages[i]
            miss +=1
        else:
            hit+=1
    #print(queue)
    return miss
    

def main():
    size = int(sys.argv[1])
    print('FIFO', FIFO(size,pages), 'page faults.')
    print( 'LRU', LRU(size,pages), 'page faults.')
    print('OPT', OPT(size,pages), 'page faults.')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()
