import sys
import os

in_file = open("in-file.xlsx", "rb") # change filename here.. opening for [r]eading as [b]inary
data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()
size=int(sys.getsizeof(data))

print size
out_file = open("out-file.xlsx", "wb") # open for [w]riting as [b]inary

out_file.write(os.urandom(size))
out_file.close()