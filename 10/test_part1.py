import pytest
import part1

def test_parse_signal():
    with open('test_input1.txt') as testin:
        signal = part1.parse_signal(testin)
    assert signal[20] == 21
    assert signal[60] == 19
    assert signal[100] == 18
    assert signal[140] == 21
    assert signal[180] == 16
    assert signal[220] == 18

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 13140

