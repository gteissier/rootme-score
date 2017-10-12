#!/usr/bin/env python2

import requests
import re
import json

class FailedRequest(Exception): pass

def get_results(user):
  r = requests.get('https://www.root-me.org/%s' % user, params={'inc': 'score', 'lang': 'fr'})
  if r.status_code != 200: raise FailedRequest(r)
  return r.content

def get_status(user):
  content = get_results(user)

  m = re.search(r'(\d+)&nbsp;Points&nbsp;', content)
  assert(m)
  score = int(m.group(1))

  problems = []
  for m in re.findall(r'\<a class="(vert|rouge)".*?(x|o)&nbsp;(.*?)<', content):
    (color, status, problem) = m
    STATUSES = {
      'x': True,
      'o': False,
    }
    assert(status in STATUSES)
    problems.append((problem, STATUSES[status]))

  return (score, problems)





if __name__ == '__main__':
  from argparse import ArgumentParser
  import sys

  users_cfg = None
  parser = ArgumentParser('Fetch root-me.org results for the given set of pseudos.')
  parser.add_argument('--users', help='JSON file where to read pseudos', required=True)
  parser.add_argument('--result', help='JSON file where to write results', default='-')

  options = parser.parse_args()
  assert('users' in options and 'result' in options)

  with open(options.users, 'rb') as f:
   pseudos = json.load(f)

  users = {}
  for pseudo in pseudos:
    try:
      (score, problems) = get_status(pseudo)
      users[pseudo] = {'score': score, 'problems': problems}
    except:
      users[pseudo] = {'score': 0, 'problems': []}

  if options.result == '-':
    f = sys.stdout
  else:
    f = open(options.result, 'wb')

  json.dump(users, f)
