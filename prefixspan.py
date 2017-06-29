#! /usr/bin/env python

"""
Usage:
    prefixspan.py (frequent | top-k) <threshold>
"""

from __future__ import print_function

import sys
from collections import defaultdict
from heapq import heappop, heappush

from docopt import docopt

import csv

# Input file name
#input_path = "input.txt"
input_path = "task_all_list.txt"

# Output file name
output_path = "output" + input_path + ".csv"

results = []

def frequent_rec(patt, mdb):
    results.append((len(mdb), patt))

    occurs = defaultdict(list)
    for (i, startpos) in mdb:
        seq = db[i]
        for j in xrange(startpos, len(seq)):
            l = occurs[seq[j]]
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, j + 1))

    for (c, newmdb) in occurs.iteritems():
        if len(newmdb) >= minsup:
            frequent_rec(patt + [c], newmdb)

def topk_rec(patt, mdb):
    heappush(results, (len(mdb), patt))
    if len(results) > k:
        heappop(results)

    occurs = defaultdict(list)
    for (i, startpos) in mdb:
        seq = db[i]
        for j in xrange(startpos, len(seq)):
            l = occurs[seq[j]]
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, j + 1))

    for (c, newmdb) in sorted(occurs.iteritems(), key=(lambda (c, newmdb): len(newmdb)), reverse=True):
        if len(results) == k and len(newmdb) <= results[0][0]:
            break

        topk_rec(patt + [c], newmdb)

if __name__ == "__main__":
    argv = docopt(__doc__)

    # db = [
        # [int(v) for v in line.rstrip().split(' ')]
        # for line in sys.stdin
    # ]

    '''
    db = [
        ["0", "1", "2", "3", "4"],
        ["1", "1", "1", "3", "4"],
        ["2", "1", "2", "2", "0"],
        ["1", "1", "1", "2", "2"],
    ]
    '''
    
    db = []
    with open(input_path) as f:
        for line in f:
            db.append(line.strip().split(" "))
            
    # -------------------------------------------------------

    if argv["frequent"]:
        minsup = int(argv["<threshold>"])
        f = frequent_rec
    elif argv["top-k"]:
        k = int(argv["<threshold>"])
        f = topk_rec

    f([], [(i, 0) for i in xrange(len(db))])

    if argv["top-k"]:
        results.sort(key=(lambda (freq, patt): (-freq, patt)))
        filtered_result = []
        for item in results:
            if len(item[1]) > 0:
                item_list = [len(item[1])*item[0], len(item[1]), item[0], item[1]]
                #filtered_result.append(item_list)
                filtered_result.append(item_list)
        
        #a = results[0][0]
        #print(filtered_result)
        #print top_k_result
        #heappop(results)
        results = filtered_result
        results.sort(key=(lambda x:x[0]), reverse=True)
        
        f = open(output_path,"wb")
        w = csv.writer(f)
        w.writerows([["score", "itemset_length", "frequency", "itemset"]])
        w.writerows(results)
        f.close()
        
    for (score, length, freq, patt) in results:
        print("{}\t{}\t{}\t{}".format(score, length, freq, patt))