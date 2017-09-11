#!/usr/bin/env python2

import json
import sys
from argparse import ArgumentParser

parser = ArgumentParser('Highlight problems that were solved by a single person.')
parser.add_argument('--result', help='JSON file where to read results', required=True)

options = parser.parse_args()

result = {}
with open(options.result, 'rb') as f:
  result = json.load(f)

problems = {}
for u in result:
  for (name, status) in result[u]['problems']:
    if status:
      if name not in problems:
        problems[name] = []
      problems[name].append(u)

unique_solvers = {}
for name in problems:
  if len(problems[name]) == 1:
    u = problems[name][0]
    if u not in unique_solvers:
      unique_solvers[u] = []
    unique_solvers[u].append(name)

for u in unique_solvers:
  print('%s is the unique solver of:' % u)
  for name in unique_solvers[u]:
    print('  %s' % name)

