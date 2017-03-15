from __future__ import print_function

import timeit

# Gives access to the highest available precision timer. 
TIMER = timeit.default_timer

class Tracer(object):
    def __init__(self, label=None, parent=None):
        self.timestamps = []
        self.label = label
        self.parent = parent

    def trace_fn(self, msg=None):
        def outer(fn):
            context = msg or fn.__name__
            def inner(*args, **kwargs):
                with self.context(msg):
                    fn(*args, **kwargs)

    def context(self, msg=None):
        return Tracer(msg, parent=self)

    def trace(self, msg=None):
        self.timestamps.append((msg, TIMER()))

    def _add_child_traces(self, child):
        self.timestamps.extend([
            ('%s :: %s' % (child.label, msg or ''), ts)
            for msg, ts in child.timestamps
        ])

    def __enter__(self):
        self.trace('>>')
        return self

    def __exit__(self, _type, _value, _traceback):
        self.trace('<<')

        if self.parent:
            self.parent._add_child_traces(self)

    def report(self):
        _, start = self.timestamps[0]
        _, end = self.timestamps[-1]

        print('Elapsed time: %.4f ms' % ((end-start) * 1000))
        last = start
        for msg, ts in self.timestamps:
            print('%-5.4f ms [of %-5.4f ms total]: %s' % (((ts-last)*1000), (ts-start)*1000, msg))  
            last = ts
