#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
Usage:
    prefixspan.py <input-file> <k-top-threshold>
"""

from __future__ import print_function

import sys
from collections import defaultdict
from heapq import heappop, heappush

from docopt import docopt

import csv
import os

# Input file name
input_path = "input.txt"
#input_path = "task_all_list.txt"

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
    #for (c, newmdb) in sorted(occurs.iteritems(), key=(lambda kv: (newmdb, len(newmdb))), reverse=True):
        if len(results) == k and len(newmdb) <= results[0][0]:
            break

        topk_rec(patt + [c], newmdb)

if __name__ == "__main__":
    
    # -------------------------------------------------------
    # Load argv
    
    argv = docopt(__doc__)

    minsup = 1
    k = int(argv["<k-top-threshold>"]) + 1 
    f = topk_rec
        
    if argv["<input-file>"]: 
        input_path = argv["<input-file>"]
    
    # ---------------------------------------------
    # Prepare data
    
    # db = [
        # [int(v) for v in line.rstrip().split(' ')]
        # for line in sys.stdin
    # ]

    if os.path.exists(input_path) == False:
        print("No file existed: " + input_path)
        quit()
    
    input_files = []
    dir = ""
    if os.path.isfile(input_path):
        input_files.append(input_path)
    else:
        dir = input_path
        for f in os.listdir(input_path):
            if f.endswith(".txt") or f.endswith(".csv"):
                input_files.append(f)
    
    if dir != "" and not os.path.exists(dir + "-output"):
        os.makedirs(dir + "-output")
    
    # ----------------------------------
        
    for input_path_item in input_files:
        results = []
        output_path = "output-" + input_path_item + ".csv"
        if dir != "":
            input_path_item = dir + "/" + input_path_item
            output_path = dir + "-output" + "/" + output_path
        
        # --------------------------------------
        print(input_path_item)
         
        db = []
        
        if input_path_item.endswith(".txt"):
            with open(input_path_item) as f:
                for line in f:
                    db.append(line.strip().split(" "))
        elif input_path_item.endswith(".csv"):
            # read file from csv
            f = open(input_path_item, 'r')
            
            # -------------------------
            # 加上先依照時間順序排序的演算法
            
            # -------------------------
            
            firstline = True
            line = []
            last_user = False
            last_seq_id = False
            seq_count = 1
            user_count = 0
            for row in csv.DictReader(f, ["user_id", "seq_id", "event"]):
                if firstline:    #skip first line
                    firstline = False
                    continue
                
                event = row["event"]
                user = row["user_id"]
                if event is not None:
                    seq_id = row["seq_id"]
                else:
                    event = row["seq_id"]
                    seq_id = seq_count
                    seq_count = seq_count + 1
                    
                if user != last_user:
                    user_count = user_count + 1
                    db.append(line)
                    line = []
                    last_seq_id = False
                
                if seq_id != last_seq_id:
                    line.append(event)
                else:
                    # merge same event
                    last_events = line[-1].split("&")
                    #print(((event in last_events), event, last_events))
                    if not event in last_events:
                        last_events.append(event)
                        line[-1] = "&".join(last_events)
                last_user = row["user_id"]
                last_seq_id = row["seq_id"]
            db.append(line)
            
        # -------------------------------------
        
        topk_rec([], [(i, 0) for i in xrange(len(db))])
        
        # --------------------------------------
        
        results.sort(key=(lambda (freq, patt): (-freq, patt)))
        #results.sort(key=(lambda kv: (-freq[1], patt[0])))
        filtered_result = []
        print("User count:" + str(user_count))
        for item in results:
            if len(item[1]) > 0:
                item_list = [len(item[1])*item[0], len(item[1]), item[0], (item[0] / float(user_count)), item[1]]
                filtered_result.append(item_list)
        
        results = filtered_result
        results.sort(key=(lambda x:x[0]), reverse=True)
        
        f = open(output_path,"wb")
        w = csv.writer(f)
        w.writerows([["score", "itemset_length", "frequency", "frequency_percent", "itemset"]])
        w.writerows(results)
        f.close()
        
        print(output_path)
        for (score, length, freq, freq_per, patt) in results:
            print("{}\t{}\t{}\t{}".format(score, length, freq, patt))