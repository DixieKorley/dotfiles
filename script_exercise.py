#! /usr/bin/env python

import os


 
os.system("grep -oh '\w*love\w*' sonnet.txt > answer.txt && wc -w answer.txt")
