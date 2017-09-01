#!/usr/bin/env python2

import json
import sys
from argparse import ArgumentParser

parser = ArgumentParser('Get users that have solved the given problem.')
parser.add_argument('--result', help='JSON file where to read results', required=True)
parser.add_argument('--problem', help='Problem name in French', required=True)


options = parser.parse_args()

result = {}
with open(options.result, 'rb') as f:
  result = json.load(f)

solvers = []
for u in result:
  for (name, status) in result[u]['problems']:
    if status and name == options.problem:
      solvers.append(u)

if len(solvers) == 0:
  print('no user has solved this one "%s". Double check the name of the problem, in French :)' % options.problem)
else:
  print('users who can contact to get a tip:')
  for u in solvers:
    print('  %s' % u)
