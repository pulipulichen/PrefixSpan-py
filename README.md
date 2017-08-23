修正自chuanconggao的PrefixSpan命令列工具

- GitHub: https://github.com/pulipulichen/PrefixSpan-py
- Install module first: `pip install docopt` or `python -m pip install docopt`
- Cannot work on Python 3. Tested on Python 2.7. https://www.python.org/downloads/release/python-2713/

# Usage
1. Put files in "input" directory. File format: https://github.com/pulipulichen/PrefixSpan-py/blob/master/input/input.txt
2. Excute prefixspan.bat
3. Get result in "input-output" directory

# Features
Based on state-of-the-art [PrefixSpan](http://www.cs.sfu.ca/~jpei/publications/span.pdf) algorithm.
Mining top-k patterns is also supported.

- 4种序列模式挖掘算法的比较分析: https://www.evernote.com/shard/s4/sh/c6996d46-b81b-4b85-abed-680da4eeefac/d755f0ec8ebdc52b4d3144c0aafe888b

PrefixSpan是一種序列模式探勘的演算法。通常含有序列資料的資料庫可分成稠密資料集與稀疏資料集。稠密資料集有大量的較長模式和較高支持度(亦即較多人共同)的頻繁模式。在稠密資料集中有許多相似的事件，例如DNA分析或著股票序列分析。

稀疏資料集主要由短模式組成，其中長模式的支持度較小，例如超級市場的交易數據集(客戶買的東西都不一樣，而且一次購物的商品不多)，使用者在網站中的瀏覽頁面序列(每個人瀏覽的內容都不一樣，而且一次不會點選太多網頁)等。

PrefixSpan改進了FreeSpan演算法，即透過前綴投影發掘序列模式。PrefixSpan的中心思想是在投影時不考慮所有可能出現的頻繁子序列，只檢查前綴序列，然後把相應的後綴投影成投影資料集。每個投影資料集中只檢查局部頻繁樣式，因此在整個過程中不需要生成候選序列。

PrefixSpan適用於稠密資料集和稀疏資料集兩種，而且在稠密資料集中比傳統的Apriori類演算法更有效率，相對的缺點是PrefixSpan實作難度較高，目前仍較少人採用。

# Tip
- I strongly encourage using PyPy instead of CPython to run the script for best performance. In my own experience, it is 9x times faster in average.
- 中文註解的做法：https://github.com/pulipulichen/PrefixSpan-py/blob/master/prefixspan.py#L2

# Todo
- 如果沒有時間資料，那就加入時間資料
- 要先以時間資料排序

