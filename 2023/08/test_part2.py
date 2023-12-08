from part2 import puzzle


def test_real():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == 16187743689077
