import time


def timeFoo(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("--- executed %r in %2.2f s ---" % (method.__name__, (te - ts)))
        return result

    return timed
