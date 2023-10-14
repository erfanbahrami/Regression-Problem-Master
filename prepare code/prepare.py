
import sys
def prepare_data(file, out, x_size, y_size):

	input = open(file, "rb")
	content = input.read()
	
	lines = content.split('\n')
	lines_ = []
	for i in range(0, len(lines)):
		lines_.append(lines[i].split(','))
	
	str = ""
	lines_ = lines_[:-1]
	for i in range(0, len(lines_) -1):
		for j in range(0, x_size):
			str += lines_[i][j]
			str += ","
		for k in range(0, y_size):
			if i != 0:
				str += lines_[i+1][k + x_size]
			else:
				str +=lines_[i][k + x_size]
			if k != y_size-1:
				str += ","
		str += "\n"

	out = open(out, "wb")
	out.write(str)

if __name__ == "__main__":
	if len(sys.argv) < 5:
		print("[-] error specify args!")
	else:
		prepare_data(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))

