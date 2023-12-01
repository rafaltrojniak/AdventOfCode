import sys

MY_SCIZORS = 'Z'
MY_PAPER = 'Y'
MY_ROCK = 'X'

EXPECT_LOSE = 'X'
EXPECT_DRAW = 'Y'
EXPECT_WIN= 'Z'

OP_ROCK = 'A'
OP_PAPER = 'B'
OP_SCIZORS = 'C'

EXPECT_RESULT_SCORE={
    EXPECT_LOSE: 0,
    EXPECT_DRAW: 3,
    EXPECT_WIN: 6
}

SHAPE_SCORE={
    MY_ROCK: 1,
    MY_PAPER: 2,
    MY_SCIZORS: 3
}

RESULT_GESTURE={
    OP_ROCK :{
        EXPECT_LOSE : MY_SCIZORS,
        EXPECT_DRAW : MY_ROCK,
        EXPECT_WIN:  MY_PAPER
        },
    OP_PAPER :{
        EXPECT_LOSE : MY_ROCK,
        EXPECT_DRAW : MY_PAPER,
        EXPECT_WIN:  MY_SCIZORS
        },
    OP_SCIZORS :{
        EXPECT_LOSE : MY_PAPER,
        EXPECT_DRAW : MY_SCIZORS,
        EXPECT_WIN:  MY_ROCK
        },
}


sum = 0
for line in sys.stdin.readlines():
    opponent, expectation = line.strip().split(' ')
    me = RESULT_GESTURE[opponent][expectation ]
    print( [opponent, me] )
    print(sum, EXPECT_RESULT_SCORE[expectation], SHAPE_SCORE[me])
    sum += EXPECT_RESULT_SCORE[expectation] + SHAPE_SCORE[me]

print(sum)
