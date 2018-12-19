#! /usr/bin/env python

import os
 
os.system("grep -oh '\w*love\w*' sonnet.txt > answer.txt && wc -w answer.txt") 
os.system("grep -oh '\w*thee\w*' sonnet.txt > answer2.txt && wc -w answer2.txt")
os.system("grep -oh '\w*to\w*' sonnet.txt > answer3.txt && wc -w answer3.txt")
os.system("grep -oh '\w*eternal\w*' sonnet.txt > answer4.txt && wc -w answer4.txt")
