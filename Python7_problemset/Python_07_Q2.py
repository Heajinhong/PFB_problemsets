#!/usr/bin/env python3
import re
nobody_read = open("Python_07_nobody.txt", "r")
contents = nobody_read.read()
sub = re.sub(r"Nobody" , "Jiyong", contents)
nobody_write = open("Jiyong.txt", "w")
nobody_write.write(sub)
# import re
# with open("Python_07_nobody.txt","r") as nobody_read, open("Jiyong.txt","w") as nobody_write:
#     for line in nobody_read:
#         sub = re.sub(r"Nobody", r"Jiyong", nobody_read)
#         nobody_write.write(sub)
# nobody_write.write()
## Find out what the problem is!
