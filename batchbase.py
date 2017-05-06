#!/usr/bin/env python
import sys
import yaml
import glob
import subprocess

num = 0

# instructions for an individual batch
class batch:
	def __init__(self, yaml, input_dir,\
		output_dir, additional_settings, codes):
		# set up a batch
		# what number batch is this in our list of batches to perform
		global num 
		num += 1
		self.number = num
		self.yaml = yaml
		self.input_dir = input_dir
		self.output_dir = output_dir
		self.additional_settings = additional_settings
		self.codes = codes
	# run the instructions for this batch
	def run(self):
		# first, find the files in the batch
		files = glob.glob(self.input_dir)
		# if files empty, log it
		if not files:
			# later need to work out logging in this case
			print("no input files found matching path: " + self.input_dir + " for batch: " + self.number)
		# if files not empty, start running each file
		# http://stackoverflow.com/a/4256153/1586231
		# need to figure out what use cases this tool will have
		# (which modules to support)
		# and work on command formatting accordingly
		# with appropriate flags
		else for file in files:
			process = subprocess.Popen('whatever','commands','we','are','using','tbd', stdout=subprocess.PIPE)
			output, error = process.communicate()

# read the yaml file
def parse_yaml(yaml):
	batches = []
	for yaml_batch in yaml:
		this_batch = batch(yaml[yaml_batch]['yaml'],\
			yaml[yaml_batch]['input_dir'],\
			yaml[yaml_batch]['output_dir'],\
			[setting for setting in yaml[yaml_batch]['additional_settings']],
			[code for code in yaml[yaml_batch]['codes']])

		print('yaml file: ' + yaml[yaml_batch]['yaml'])
		print('input dir: ' + yaml[yaml_batch]['input_dir'])
		for setting in yaml[yaml_batch]['additional_settings']:
			print('setting: ' + setting)
		for code in yaml[yaml_batch]['codes']:
			print('code: ' + code)
		batches.append(this_batch)
	return batches

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