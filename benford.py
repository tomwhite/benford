#!/usr/bin/python

import sys,string,math

total = 0.0
observed = [0] * 9
while 1:
  line = sys.stdin.readline()
  if not line:
    break
  if string.find('123456789', line[0]) != -1:
    d = string.atoi(line[0])
    observed[d - 1] = observed[d - 1] + 1
    total = total + 1

x2 = 0.0
i = 1
for d in observed:
  expected = math.log10(1 + 1.0 / i) * total
  print i, d, d * 100 /total, expected
  i = i + 1
  x2 = x2 + (d - expected) * (d - expected) / expected
print x2
if x2 <= 2.733:
  print "Conforms to Benford's law."
else:
  print "Does not conform to Benford's law."

