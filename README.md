# Follow your friends rootme score and solved problems

## Retrieve status from root-me.org

First you have fill a JSON array with pseudos you want to track. An example `users.json` could be:

```
[
  "hacker1",
  "poorboy",
  ...
]
```

Next, you can extract status from root-me.org using:

```
$ ./refresh-status.py --users users.json --result result.json
```

The resulting file will contain:

* score
* status of all problems, solved or not

## Follow users progress

Once you have a working `users.json`, you can diff snapshots of results:

```
$ ./diff-results.py --previous=result-0.json --current=result.json
```

It will print on stdout a diff, starting with people who have scored, biggest progress first:

```
hacker1: 123
  Javascript - Obfuscation 3
  ELF x64 - Anti-debug et equations
  XMPP - Authentification
```

Next you will find users that have not solved a single problem:

```
poorboy: you will do better next time
```

And last, people who have recently joined the group of tracked users:

```
welcome to new challenger dhalsim
```
