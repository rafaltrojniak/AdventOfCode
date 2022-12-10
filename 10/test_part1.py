import pytest
import part1

def test_parse_signal():
    with open('test_input1.txt') as testin:
        signal = part1.parse_signal(testin)
    assert signal[19] == 21
    assert signal[59] == 19
    assert signal[99] == 18
    assert signal[139] == 21
    assert signal[179] == 16
    assert signal[219] == 18

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 13140


def test_real():
    with open('input.txt') as testin:
        assert part1.run(testin) == 12540
