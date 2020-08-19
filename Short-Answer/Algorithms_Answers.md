#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1)

The variable 'a' is changed by a constant value in this function, therefore it is O(1).

- - - - - 

ANS: O(n)

b) O(n^2)

The variable 'sum' increases by 1 for every increment in range 'n', therefor the runtime is dependent on the range of 'n'. Since 'sum' changes while 'j' is also being multiplied and the function depends on 'j' being less than 'n', there are two values being iterated which leads to an n^2 runtime. 

- - - - -

ANS: O(nlog(n))

c) O(n)

The function performs recursion, which has a runtime depdendent on the value of 'bunnies'. Since the runtime does not decrease a substantial amount (from 'bunnies-1') if 'bunnies' was a large number, 'bunnies-1' becomes negligible meaning this runtime cannot be O(log(n)).

## Exercise II

I would use binary search to determine what the smallest value for f is given the egg would break at that value. If we gussed a value of f, the algorithm would determine whether or not that value breaks the egg and could cut the number of floors in half for every iteration of the binary search. This would ensure that the number of dropped and broken eggs is minimized. The runtime for this code would be O(log(n)).
