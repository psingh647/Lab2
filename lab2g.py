#!/usr/bin/env python3
#Author: Prabhnoor Singh
#Author ID: psingh647
#Date Created: 2024/04/09
import sys

if len(sys.argv) == 2: 
    timer = int(sys.argv[1])
else:    
    timer = 3


while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!') 
