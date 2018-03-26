#!/usr/bin/env python
import sys, math
r = float(sys.argv[1])
s = math.sin(r)
#print ('Hello, World! sin(%g)=%g') % (r, s)
print ('Hello, World! sin({0!r})={1!s}'.format(r, s))
