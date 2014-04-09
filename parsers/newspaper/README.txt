Currently, we have moved to the stage of gathering and comparing articles in
the real database table:

Database: Newshub
Table: articles

You need the key set from AWS to run the program and please set the path accordingly.

URL for Database: newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com
Port: 3306

How to run:
1. python fetch.py
2. python detect.py
3. python exe_prepare.py
4. python compare.py

Hints: due to the huge number of articles, the "newspaper" module may sometimes run
into problems from reading the list_en.txt and list_cn.txt and therefore, throw
exceptions in running. When this happens, simply run the program (fetch.py and detect.py)
again and it will continue from the point where exception occurs. Since we have set
the program to ignore duplicates in fetch.py, there is no need to worry about this
issue in the fetching stage.
