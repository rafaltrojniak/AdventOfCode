import pytest
import part2

def test_test_input():
    with open('test_input2.txt') as testin:
        assert part2.run(testin) == 36

def test_test_input_sim():
    with open('test_input_2_sim.txt') as testin:
        assert part2.run(testin) == 1

def test_real():
    with open('input.txt') as testin:
        assert part2.run(testin) == 2630


def test_step_1():
    rope_before=[(1,0),(0,0)]
    expedted_rope_after=[(2,0),(1,0)]

    rope_after = part2.run_step(1,0,rope_before)
    part2.print_board(rope_before)
    part2.print_board(rope_after)
    assert rope_after == expedted_rope_after

def test_step_2():
    rope_before=[(0,0),(0,1)]
    expedted_rope_after=[(0,-1),(0,0)]

    rope_after = part2.run_step(0,-1,rope_before)
    part2.print_board(rope_before)
    part2.print_board(rope_after)
    assert rope_after == expedted_rope_after

def test_step_3():
    rope_before=[(0,0),(-1,-1)]
    expedted_rope_after=[(0,1),(0,0)]

    rope_after = part2.run_step(0,1,rope_before)
    x_range=range(-2,2)
    y_range=range(-2,2)
    print('before')
    part2.print_board(rope_before, x_range=x_range, y_range=y_range)
    print('expected')
    part2.print_board(expedted_rope_after, x_range=x_range, y_range=y_range)
    print('after')
    part2.print_board(rope_after, x_range=x_range, y_range=y_range)
    assert rope_after == expedted_rope_after

def test_step_4():
    rope_before=[(0,0),(-1,-1)]
    expedted_rope_after=[(1,0),(0,0)]

    rope_after = part2.run_step(1,0,rope_before)
    x_range=range(-2,2)
    y_range=range(-2,2)
    print('before')
    part2.print_board(rope_before, x_range=x_range, y_range=y_range)
    print('expected')
    part2.print_board(expedted_rope_after, x_range=x_range, y_range=y_range)
    print('after')
    part2.print_board(rope_after, x_range=x_range, y_range=y_range)
    assert rope_after == expedted_rope_after

def test_circle():
    rope_before=[(0,0),(-1,-1)]
    expedted_rope_after=[(-1,0),(-1,-1)]

    rope_after = part2.run_step(-1,0,rope_before)

    x_range=range(-2,1)
    y_range=range(-2,1)
    print('before')
    part2.print_board(rope_before, x_range=x_range, y_range=y_range)
    print('expected')
    part2.print_board(expedted_rope_after, x_range=x_range, y_range=y_range)
    print('after')
    part2.print_board(rope_after, x_range=x_range, y_range=y_range)
    assert rope_after == expedted_rope_after

def test_chain():
    #......
    #....H.
    #4321..  (4 covers 5, 6, 7, 8, 9, s)
    rope_before=[(5,2),(4,1),(3,1),(2,1),(1,1),(1,1),(1,1)]
    #....H.
    #.4321.
    #5.....  (5 covers 6, 7, 8, 9, s)
    expedted_rope_after=[(5,3),(5,2),(4,2),(3,2),(2,2),(1,1),(1,1)]

    rope_after = part2.run_step(0,1,rope_before)

    x_range=range(1,6)
    y_range=range(1,4)
    print('before')
    part2.print_board(rope_before, x_range=x_range, y_range=y_range)
    print('expected')
    part2.print_board(expedted_rope_after, x_range=x_range, y_range=y_range)
    print('after')
    part2.print_board(rope_after, x_range=x_range, y_range=y_range)
    assert rope_after == expedted_rope_after

def test_chain2():
    #......
    #....H.
    #.4321.
    #5.....  (5 covers 6, 7, 8, 9, s)
    rope_before=[(5,3),(5,2),(4,2),(3,2),(2,2),(1,1),(1,1)]
    #......
    #....H.
    #....1.
    #.432..
    #5.....  (5 covers 6, 7, 8, 9, s)
    expedted_rope_after=[(5,4),(5,3),(4,2),(3,2),(2,2),(1,1),(1,1)]

    rope_after = part2.run_step(0,1,rope_before)

    x_range=range(1,6)
    y_range=range(1,4)
    print('before')
    part2.print_board(rope_before, x_range=x_range, y_range=y_range)
    print('expected')
    part2.print_board(expedted_rope_after, x_range=x_range, y_range=y_range)
    print('after')
    part2.print_board(rope_after, x_range=x_range, y_range=y_range)
    assert rope_after == expedted_rope_after

def test_chain3():
    #......
    #....H.
    #....1.
    #.432..
    #5.....  (5 covers 6, 7, 8, 9, s)
    rope_before=[(5,4),(5,3),(4,2),(3,2),(2,2),(1,1),(1,1)]
    #....H.
    #....1.
    #..432.
    #.5....
#    6.....  (6 covers 7, 8, 9, s)
    expedted_rope_after=[(5,5),(5,4),(5,3),(4,3),(3,3),(2,2),(1,1)]

    rope_after = part2.run_step(0,1,rope_before)

    x_range=range(1,6)
    y_range=range(1,7)
    print('before')
    part2.print_board(rope_before, x_range=x_range, y_range=y_range)
    print('expected')
    part2.print_board(expedted_rope_after, x_range=x_range, y_range=y_range)
    print('after')
    part2.print_board(rope_after, x_range=x_range, y_range=y_range)
    assert rope_after == expedted_rope_after
