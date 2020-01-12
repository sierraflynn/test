#!/usr/bin/python
import os
#import datetime
#import numpy
import re
import argparse

def isAnagram(word):
    if word == word[::-1]:
        return True
    return False

if __name__== "__main__":
    print isAnagram("mom")
    print isAnagram("watermellon")