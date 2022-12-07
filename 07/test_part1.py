import pytest
import part1

def test_test_input():
    with open('test_input1.txt') as testin:
        assert part1.run(testin) == 95437

def test_real():
    with open('input.txt') as testin:
        assert part1.run(testin)== 1118405

def test_read_tree():
    tree={
      "a": {
        "e": {
          "i":584,
        },
        "f":29116,
        "g":2557,
        "h.lst":62596,
      },
      "b.txt":14848514,
      "c.dat":8504156,
      "d": {
        "j":4060174,
        "d.log":8033020,
        "d.ext":5626152,
        "k":7214296,
        }
    }

    with open('test_input1.txt') as testin:
        assert part1.read_tree(testin) == tree
