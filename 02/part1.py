import sys

MY_SCIZORS = 'Z'
MY_PAPER = 'Y'
MY_ROCK = 'X'
OP_ROCK = 'A'
OP_PAPER = 'B'
OP_SCIZORS = 'C'

SHAPE_SCORE={
    MY_ROCK: 1,
    MY_PAPER: 2,
    MY_SCIZORS: 3
}

RESULT_SCORE={
    OP_ROCK :{
        MY_ROCK: 3,
        MY_PAPER: 6,
        MY_SCIZORS: 0
        },
    OP_PAPER :{
        MY_ROCK: 0,
        MY_PAPER: 3,
        MY_SCIZORS: 6
        },
    OP_SCIZORS :{
        MY_ROCK: 6,
        MY_PAPER: 0,
        MY_SCIZORS: 3
        },
}

sum = 0
for line in sys.stdin.readlines():
    opponent, me = line.strip().split(' ')
    print( [opponent, me])
    print(sum, RESULT_SCORE[opponent][me], SHAPE_SCORE[me])
    sum += RESULT_SCORE[opponent][me] + SHAPE_SCORE[me]

print(sum)
