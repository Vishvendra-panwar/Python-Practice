# Files Read and writes examples.

### Printing file lines #####

"""
filename = 'D:\\z.Tmp\\numbers.txt'

with open(filename, 'r') as fh:
    for line in fh:
        print(line)
"""
##### Taking filename input from User #####

"""
import sys

def main():
    if len(sys.argv) !=2:
        exit("Usages : " + sys.argv[0] + " FileName")
    filename = sys.argv[1]
    with open(filename) as fh:
        print("Working on the file", filename)
        for line in fh:
            print(line)

main()
"""

#### File Handle with or without ####


"""
filename = 'D://z.Tmp//numbers.txt'

fh = open(filename, 'r')
print(fh)
data = fh.read()
print(data)
fh.close()
print(fh)

with open(filename,'r') as fh:
    print(fh)
    data = fh.read()
    print (data)
print(fh)
//
"""

#### File Handle with return ####

"""
import sys

def process_file(filename):
    with open(filename, 'r') as fh:

        for line in fh:
            line = line.rstrip("\n")
            if len(line) > 0:
                if line[0] == '#':
                    return
            
            if len(line) > 1:
                if line[0:2] =='//':
                    return
            
            print(line)

process_file(sys.argv[0])

"""

### Read all the lines into a list ###
filename = 'D://z.Tmp//numbers.txt'

with open(filename, 'r') as fh:
    lines_list = fh.readlines()

# print numers of lines
print(len(lines_list))
print(lines_list)
for line in lines_list:
    print(line, end="")