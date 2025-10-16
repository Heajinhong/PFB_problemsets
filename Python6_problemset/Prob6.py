#!/usr/bin/env python3
#problem1
# text_file = open("Python_06.txt","r")
# for tx in text_file:
#     line = tx.upper()
#     print(line)
# text_file.close()

#problem2
with open("Python_06.txt","r") as text_read, open("Python_06_uc.txt", "w") as text_write:
    for tx in text_read:
        tx = tx.rstrip()
        line = tx.upper()
        text_write.write(f"{line}\n")
