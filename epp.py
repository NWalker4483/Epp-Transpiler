import re
# Read in input file argument
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input", '-i', required=True, type=str, help="echo the string you use here")
args = parser.parse_args()
# Read CodeString
with open(args.input,'r') as code: 
    original_program = code.readlines()
# Isolate special characters with white space
spec_char = ["*","=","-","+",">","<","[","]","(",")","{","}",",",";"]
spec_dbl_char = ["==","++","--","+=","-=","<=",">="]
spaced_program = []
includes = []
for line in original_program:
    # Skip includes and existing defines
    if line[0]=='#':
        includes.append(line)
        continue
    # Remove comments 
    if "//" in line:
        line = line[:line.find('//')]
        if len(line.strip()) == 0:
            continue
    # TODO: Add handler for string constants
    split_line = line
    for char in spec_char:
        split_line = re.sub('\{}'.format(char)," "+char+" ", split_line)
        split_line = " ".join(split_line.split())
    # Correct the spliting of double chars
    for char in spec_dbl_char:
        split_line = re.sub('\{} \{}'.format(char[0],char[1])," "+char+" ", split_line)
        split_line = " ".join(split_line.split())
    spaced_program.append(split_line)
# Generate word set 
wordset = set() 
for term in " ".join(spaced_program).split():
    wordset.add(term)
# Store wordset as dictionary with definitions
name = 'e'
worddict = dict()
for word in wordset:
    worddict[word] = name
    name += 'e'

# Write defines to output file
temp = args.input.split('.')
out_filename = "".join([temp[0],".epp.",temp[1]])
with open(out_filename,'w') as output:
    for word in worddict:
        output.write("#define ")
        output.write(worddict[word])
        output.write(" ")
        output.write(word)
        output.write("\n")
    output.write("\n")
    for i in includes:
        output.write(i)
        output.write("\n")
    for line in spaced_program:
        for word in line.split():
            try:
                output.write(worddict[word])
                output.write(" ")
            except:
                pass
        output.write("\n")
        
