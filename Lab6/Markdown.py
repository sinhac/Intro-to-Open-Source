"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  if (line.startswith('#')) 
    line = "<h1>" + line[1:] + "/h1"

def convertH2(line):
  if (line.startswith('##')) 
    line = "<h2>" + line[1:] + "/h2"

def convertH3(line):
  if (line.startswith('###')) 
    line = "<h3>" + line[1:] + "/h3"


for line in fileinput.input():
  line = line.rstrip() def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')
    
  line = convertStrong(line)
  line = convertEm(line)
  print '<p>' + line + '</p>',