-include_lib("eunit/include/eunit.hrl").
-module('test_part1').

find_calibration_test() ->
  ?assertEqual(12, part1:find_calibration("1abc2")).

solve_single_test() ->
  ?assertEqual(12, part1:solve(["1abc2"])).

solve_two_test()->
  ?assertEqual(46, part1:solve(["1abc2","3abc4"])).

solve_example_test()->
  ?assertEqual(142, part1:solve([
"1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet"
  ])).

find_first_test() ->
  ?assertEqual(1, part1:find_first("1abc2")).

find_last_test() ->
  ?assertEqual(2, part1:find_last("1abc2")).
