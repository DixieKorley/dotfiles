#! /usr/bin/env python

import os
 
os.system("grep -oh -e '\w*love\w*' -e '\w*thee\w*' -e '\w*to\w*' -e '\w*eternal\w*' sonnet.txt > answer_final.txt && wc -w answer_final.txt") 



