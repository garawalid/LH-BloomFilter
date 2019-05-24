from lhbf.hash_function import hash_int, hash_str


def test_hash_str():
    examples = ["word1", "WORD_2", "123456"]

    expected_results = [2341, 4429, 2881]

    for i in range(len(examples)):
        assert (hash_str(examples[i], p=53, m=1000), expected_results[i])


def test_hash_int():
    examples = [156, 0, 16543, -200]

    expected_results = [771, 0, 81793, 988]

    for i in range(len(examples)):
        assert (hash_int(examples[i], p=3), expected_results[i])
