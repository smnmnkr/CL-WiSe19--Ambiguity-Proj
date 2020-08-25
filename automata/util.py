import itertools


# -------- create_strings -----------
#
def create_strings(chars: list, n: int) -> Iterable:

    for item in itertools.product(chars, repeat=n):
        yield "".join(item)