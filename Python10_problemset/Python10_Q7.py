#!/usr/bin/env python3
import subprocess
subprocess.run(["ls", "-l"])
output = subprocess.check_output('ls -l | grep 1', shell = True)