#!/usr/bin/env python2

import json
import sys
from argparse import ArgumentParser

parser = ArgumentParser('Diff root-me.org results.')
parser.add_argument('--previous', help='JSON file where to read base results', required=True)
parser.add_argument('--current', help='JSON file where to read current results', default=None)


options = parser.parse_args()
assert('previous' in options and 'current' in options)

previous = {}
with open(options.previous, 'rb') as f:
  previous = json.load(f)

current = {}
with open(options.current, 'rb') as f:
  current = json.load(f)

previous_users = set([u for u in previous])
current_users = set([u for u in current])

new_users = current_users - previous_users
already_users = current_users & previous_users

progresses = {}
for u in already_users:
  progresses[u] = {
    'delta': current[u]['score'] - previous[u]['score']
  }

  current_solved = set([p[0] for p in current[u]['problems'] if p[1]])
  previous_solved = set([p[0] for p in previous[u]['problems'] if p[1]])

  progresses[u]['solved_problems'] = current_solved-previous_solved

sorted_progresses = sorted([(k, progresses[k]['delta']) for k in progresses], key=lambda x: x[1],
  reverse=True)

for (k, delta) in sorted_progresses:
  print('%s: %d' % (k, delta))
  for p in progresses[k]['solved_problems']:
    print('  %s' % p)

for u in new_users:
  print('welcome new challenger %s' % u)
