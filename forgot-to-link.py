#!/usr/bin/env python3
import sys
import os
import re
from google import google

pattern = re.compile("\[.+?\]")

def get_link(keyword):
	results = google.search(keyword, 1)
	if results:
		print("'{}' -> {}".format(keyword, results[0].link))
		return results[0].link
	else:
		return ""

def process_line(line):
	i = 0
	line2 = ""
	while i < len(line):
		m = pattern.search(line, i)
		if m:
			s,e = m.span()
			line2 += line[i:e]
			if e >= len(line) or line[e] != '(':
				link = get_link(line[s+1:e-1])
				line2 += '(' + link + ')'
			i = e
		else:
			line2 += line[i:]
			break
	return line2

def process_file(src_file, dst_file):
	sf = open(src_file, "rt")
	df = open(dst_file, "wt")
	for line in sf:
		line2 = process_line(line)
		df.write(line2)
	df.close()
	sf.close()

if __name__ == '__main__':
	src_file = sys.argv[1]
	dst_file = sys.argv[2]
	print("process", src_file, "->", dst_file)
	process_file(src_file, dst_file)
