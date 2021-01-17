from itertools import groupby
def pack(l):
    return [list(group) for key, group in groupby(l)]