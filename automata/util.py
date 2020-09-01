import itertools


# -------- create_permutations -----------
#
def create_permutations(chars: list, n: int):

    for item in itertools.product(chars, repeat=n):
        yield "".join(item)
