import subprocess
import re

filename = 'test2.cpp'
name_len = len(filename)
out = subprocess.Popen(['flawfinder', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
stdout = stdout.decode("utf-8")
r = re.compile('[^:]+:(\\d+):\\s+\\[(\\d+)\\]\\s+([^:]+):\n((?:  .*\n)+)')
result = r.findall(stdout)
for i in range(len(result)):
	result[i] = list(result[i])
	result[i][3] = result[i][3].replace('\n  ', ' ').strip()
print(result)