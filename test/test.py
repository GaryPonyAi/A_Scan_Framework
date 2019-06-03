import subprocess
import re

filename = 'test9.cpp'
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
# description = '\n'.join([i[3] for i in result])

# print('\n'.join([i[3] for i in result]))
# description = ""
# for i in range(len(result)):
# 	print(result[i][3])
# 	description.append(result[i][3])
# print(description)

# with open('test9.cpp', 'r') as f:
#     content = f.read()

# # (?# r = re.compile(r'\b(\w+)\([^{]+\{(.+)}'))
# # result = r.findall(content)
# print(re.findall(r'\b(\w+)\([^{]+\{(.+)}', content, re.S))