# tinytrace
Teeny tiny timing module for tracing execution time in python.

Not quite ready for real use yet

```python
import tinytrace as tt

t = tt.Tracer('tracer_example')

def really_slow(n):
    [i for i in range(10 ** n) if i == 1]


t.trace('starting trace')

with t.context('really_slow_fn') as t1:
    for n in range(5, 8):
        t1.trace('START really_slow(%d)' % n)
        really_slow(n)
        t1.trace('FINISH really_slow(%d)' % n)
    
t.trace('finished trace')

t.report()

# Elapsed time: 507.1900 ms
#    0.0000 ms [of    0.0000 ms total]: starting trace
#    0.1318 ms [of    0.1318 ms total]: really_slow_fn :: >>
#    0.0191 ms [of    0.1509 ms total]: really_slow_fn :: START really_slow(5)
#    5.0039 ms [of    5.1548 ms total]: really_slow_fn :: FINISH really_slow(5)
#    0.0010 ms [of    5.1558 ms total]: really_slow_fn :: START really_slow(6)
#   48.3251 ms [of   53.4809 ms total]: really_slow_fn :: FINISH really_slow(6)
#    0.0050 ms [of   53.4859 ms total]: really_slow_fn :: START really_slow(7)
#  453.5429 ms [of  507.0288 ms total]: really_slow_fn :: FINISH really_slow(7)
#    0.0081 ms [of  507.0369 ms total]: really_slow_fn :: <<
#    0.1531 ms [of  507.1900 ms total]: finished trace
```
