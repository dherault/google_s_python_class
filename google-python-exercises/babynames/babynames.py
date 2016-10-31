#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

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

def by_name(list):
  return list[0]

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename)
  html = f.read()

  # Could also use the filename
  year_match = re.search(r'Popularity in (\d*)', html)

  if (not year_match):
    print 'No year_match u_u'
    return

  year = year_match.group(1)

  names_tuples = re.findall(r'<tr align="right"><td>(\d+)</td><td>([\w\s-]+)</td><td>([\w\s-]+)</td>', html)

  if (not names_tuples):
    print 'No names_tuples u_u'
    return

  names_dict = {}

  for rank, male, female in names_tuples:

    if male in names_dict:
      existing_rank = names_dict[male]
      # print 'Found dupl: ' + male + ' ' + rank + ' ' + existing_rank

      if existing_rank > rank: names_dict[male] = rank

    else: names_dict[male] = rank

    if female in names_dict:
      existing_rank = names_dict[female]
      # print 'Found dupl: ' + female + ' ' + rank + ' ' + existing_rank

      if existing_rank > rank: names_dict[female] = rank

    else: names_dict[male] = rank

  results = [year]

  for key in sorted(names_dict.keys()):
    results.append(key + ' ' + names_dict[key])

  return results


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  print '\n'.join(extract_names(args[0])) + '\n'

if __name__ == '__main__':
  main()
