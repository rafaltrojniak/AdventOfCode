-module('part1').
-export([solve/1, find_first/1, find_last/1, find_calibration/1, main/1]).
-include_lib("eunit/include/eunit.hrl").


find_first([Letter|Tail]) when Letter > $9 -> 
  find_first(Tail);
find_first([Letter|Tail]) when Letter < $0 -> 
  find_first(Tail);
find_first([]) -> 
  erlang:raise(error, 'No digit found');
find_first([Letter|_Tail]) -> 
  Letter - $0.

find_last(List) ->
  find_first(lists:reverse(List)).

find_calibration([]) -> 0;
find_calibration(Data) ->
  First = find_first(Data),
  Last = find_last(Data),
  First*10 + Last.

solve(Data) ->
%  Calibrations = lists:map(fun(X) -> find_calibration(X) end, Data),
  Calibrations = [  find_calibration(X)|| X <- Data],
  lists:foldl(fun(X, Sum) -> X + Sum end, 0, Calibrations).


main(_Test) ->
   {ok, Binary} = file:read_file("input.txt"),
   % Last element is empty list [], how to remove it ?
   Text = [binary_to_list(Bin) || Bin <- binary:split(Binary,<<"\n">>,[global])],
   io:fwrite("~p~n",[Text]),
   Solution=solve(Text),
   io:fwrite("~p~n",[Solution]).
