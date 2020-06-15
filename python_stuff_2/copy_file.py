#!/usr/bin/python3

import sys

try:
    read_alice_fh = open(sys.argv[0], 'r')
    
except Exception as e:
    sys.stderr.write(str(e))

if read_alice_fh is None:
    sys.stderr.write("Failed to open file {0}".format(alice.txt))

write_alice_copy = open("alice.txt.copy", 'w')

for line in read_alice_fh:
    write_alice_copy.write(line)



read_alice_fh.close()
write_alice_copy.close() 
    
    

