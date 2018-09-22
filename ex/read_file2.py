import sys

def process_file(filename):
	"""Open,read and print file"""
	input_file = open(fliename,"r")
	for line in input_file:
		line = line.strip()
		print(line)
	input_file.close()

if __name__ == "__main__":
	process_file(sys.argv[1],"r")
