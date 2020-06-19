#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - number of operations increases proportionally related to size of input


b) O(nlogn) - output grows slightly faster than proportional (On) but not at a O(n^2) rate


c)O(n) - number of operations increases proportionally related to size of input

## Exercise II


Building Attributes- 
We have a building of undisclosed stories
A floor at f or higher will cause fallen eggs to break
A floor lower than f won't cause fallen eggs to break

Eggs Behavior - 
We have some quantity of eggs
Some eggs will fall some won't
Eggs can fall off of stories
Eggs will break if they fall off at f story and higher
Eggs won't break if they fall off lower than story f

Pseudo Code
Go to each floor dropping an egg from it as we go. If the egg breaks that's the floor we are looking for. If it doesn't proceed to the next floor and continue dropping. The complexity of this is O(n) - in the worst case because the floor we are looking for could be equal to n(the top floor)

If we didn't care about the number breakages and wanted the least number of trials we could apply a binary search pattern to the problem to achieve an O(log n) solution
