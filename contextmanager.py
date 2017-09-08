from contextlib import contextmanager


class counter(object):
    def __init__(self):
        self.count = 0


@contextmanager
def onemore(obj):
    try:
        obj.count += 1
        yield
    finally:
        obj.count -= 1


c1 = counter()

# within this block c1 has one higher count than outside
with onemore(c1):
    print(c1.count)

print(c1.count)
