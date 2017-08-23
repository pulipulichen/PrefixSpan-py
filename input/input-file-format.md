Input File Format
====

# Text format: input.txt
https://github.com/pulipulichen/PrefixSpan-py/blob/master/input/input.txt

````
0 1 2 3 4 0
1 1 1 3 4
2 1 2 2
1 1 1 2 2
````

In "input.txt" data set, each people splited by lines and each actions splited by space. It means there are 4 people in "input.txt" data set.

First one did 6 actions, coded "0", "1", "2", "3", "4" and "0".

Second one did 5 actions, coded "1", "1", "1", "3" and "4".

Third one did 4 actions, coded "2", "1", "2" and "2".

Last one did 5 actions, coded "1", "1", "1", "2" and "2".

-----

# CSV format: input.csv

https://github.com/pulipulichen/PrefixSpan-py/blob/master/input/input.csv

````
user_id,seq_id,events
User1,123814,start_exp
User1,124046,GL1_4
User1,124046,GL5_5
User1,124046,GL5_6
````