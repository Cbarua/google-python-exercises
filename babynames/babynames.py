#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename, 'r')
  filecontent = f.read()
  # - Extract the year and print it
  # year = re.findall(r'<h3.*(\d{4})</h3>', f.read())
  # year = re.findall(r'\d{4}', filename)
  year = re.findall(r'Popularity\sin\s(\d\d\d\d)', filecontent)

  # - Extract the names and rank numbers and just print them
  # names = re.findall(r'<h3.*(\d{4})</h3>[\S\s]*<td>(\d).*<td>([a-zA-Z]+).*<td>([a-zA-Z]+)', f.read())
  data = re.findall(r'<td>(\d+).*<td>([a-zA-Z]+).*<td>([a-zA-Z]+)', filecontent)
  f.close()

  # - Get the names data into a dict and print it
  # dict_names = {}
  # for rank, male, female in data:
  #   dict_names[int(rank)] = [male, female]
  # print(dict_names)
  
  # - Remove duplicate names
  names = set()
  # - Build the [year, 'name rank', ... ] list and print it
  result = year + []

  for rank, male, female in data:
    if male not in names:
      result.append(f'{male} {rank}')
    else:
      print(f'Duplicate name: {male} {rank}')
    if female not in names:
      result.append(f'{female} {rank}')
    else:
      print(f'Duplicate name: {female} {rank}')

    names.add(male)
    names.add(female)

  result = sorted(result)
  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  if '*' in args[0]:
    partials = args[0].split('*')
    filelist = os.listdir(os.getcwd())
    pattern = f'^{partials[0]}.*{partials[1]}$'
    filtered_filelist = [s for s in filelist if re.match(pattern, s)]
    args = filtered_filelist


  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for a in args:
    names = extract_names(a)
    output = '\n'.join(names) + '\n'
    if summary:
      f = open(f'./{a}.summary', 'w')
      f.write(a + '\n' + '-' * len(a) + '\n')
      f.write(output)
      f.close()
    else:
      print(output)

if __name__ == '__main__':
  main()
