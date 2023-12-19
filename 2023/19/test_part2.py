import pytest

from part2 import puzzle, parse_input, normalise_edges, agg_rules_into_ranges

example_input = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

parsed_input = (
    {
        'px': [("a", "<", 2006, "qkq"), ("m", ">", 2090, "A"), ("rfg",)],
        'pv': [("a", ">", 1716, "R"), ("A",)],
        'lnx': [("m", ">", 1548, "A"), ("A",)],
        'rfg': [("s", "<", 537, "gd"), ("x", ">", 2440, "R"), ("A",)],
        'qs': [("s", ">", 3448, "A"), ("lnx",)],
        'qkq': [("x", "<", 1416, "A"), ("crn",)],
        'crn': [("x", ">", 2662, "A"), ("R",)],
        'in': [("s", "<", 1351, "px"), ("qqz",)],
        'qqz': [("s", ">", 2770, "qs"), ("m", "<", 1801, "hdj"), ("R",)],
        'gd': [("a", ">", 3333, "R"), ("R",)],
        'hdj': [("m", ">", 838, "A"), ("pv",)],
    },
    [
        {"x": 787, "m": 2655, "a": 1222, "s": 2876},
        {"x": 1679, "m": 44, "a": 2067, "s": 496},
        {"x": 2036, "m": 264, "a": 79, "s": 2244},
        {"x": 2461, "m": 1339, "a": 466, "s": 291},
        {"x": 2127, "m": 1623, "a": 2188, "s": 1013}
    ]
)

example_response = 167409079868000


def test_example_parsing():
    assert parse_input(example_input) == parsed_input


# @pytest.mark.skip()
def test_example():
    assert puzzle(example_input) == example_response


@pytest.mark.skip()
def test_real_right_response():
    with open('input.txt', 'r') as indata:
        assert puzzle(indata.read()) == None


def test_normalise_edges():
    assert normalise_edges([("s", ">", 2770, "qs"), ("m", "<", 1801, "hdj"), ("R",)]) == \
           [
               ("qs", (("s", ">", 2770),)),
               ("hdj", (("s", "<", 2771), ("m", "<", 1801))),
               ("R", (("s", "<", 2771), ("m", ">", 1800)))
           ]


def test_agg_rules_into_ranges():
    assert agg_rules_into_ranges((('s', '<', 1351),
                                  ('a', '<', 2006),
                                  ('x', '>', 1415),
                                  ('x', '>', 2662))
                                 ) == \
           {'x': (2663, 4000),
            'm': (1, 4000),
            'a': (1, 2005),
            's': (1, 1350)
            }
