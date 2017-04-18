#!/usr/bin/env python
import sys
import yaml

# read the yaml file
def parse_yaml(yaml):
	print('hello')

# handle command line args
def main(argv):
	with open(argv[0]) as stream:
		try:
			parse_yaml(yaml.load(stream))
			return 0
		except yaml.YAMLError as exc:
			print(exc)
			return 1

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))