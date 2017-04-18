#!/usr/bin/env python
import yaml
import fileinput

def process(line):
	print(line)

for line in fileinput.input():
    process(line)