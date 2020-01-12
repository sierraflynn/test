#!/usr/bin/python
import os
#import datetime
#import numpy
import re
import argparse

def isAnagram(word):
    for i in range(len(word)):
        print word[i] + ' ' + word[len(word)-1-i]
        if word[i] != word[len(word)-1-i]:
            return False
    return True

if __name__== "__main__":
    print isAnagram("mom")