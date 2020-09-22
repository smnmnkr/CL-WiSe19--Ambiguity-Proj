from automata.util import create_permutations

alphabet_1: list = ["a"]
alphabet_2: list = ["a", "b"]


def test_create_permutations_n1():
    assert set(create_permutations(alphabet_1, 1)) == set(alphabet_1)
    assert set(create_permutations(alphabet_2, 1)) == set(alphabet_2)


def test_create_permutations_n2():
    assert set(create_permutations(alphabet_1, 2)) == {"aa"}
    assert set(create_permutations(alphabet_2, 2)) == {
        "ab",
        "ba",
        "aa",
        "bb",
    }
