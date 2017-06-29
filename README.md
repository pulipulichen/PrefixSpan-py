修正自chuanconggao的PrefixSpan命令列工具

- GitHub: https://github.com/pulipulichen/PrefixSpan-py

# Usage
Just replace the variable `db` with your own sequences, and variable `minsup` with your own minimum support threshold.

# Features
Based on state-of-the-art [PrefixSpan](http://www.cs.sfu.ca/~jpei/publications/span.pdf) algorithm.
Mining top-k patterns is also supported.
- 4种序列模式挖掘算法的比较分析: https://www.evernote.com/shard/s4/sh/c6996d46-b81b-4b85-abed-680da4eeefac/d755f0ec8ebdc52b4d3144c0aafe888b

# Tip
I strongly encourage using PyPy instead of CPython to run the script for best performance. In my own experience, it is 9x times faster in average.

# Todo
- 如果沒有時間資料，那就加入時間資料
- 要先以時間資料排序
