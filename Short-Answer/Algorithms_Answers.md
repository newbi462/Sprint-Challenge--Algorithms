#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
* Should be O(n) because the ```while (a < n * n * n)``` is more in relation to ```a``` there is no math here that would change the A to N relation as ```n * n * n``` and ```a + n * n``` are 1 and so on extenders not modifiers of the O(n)


b)O(n log n)
* While a loop in a loop would default to n^2, in this case the ```while j < n:``` is cut by half with each loop ```j *= 2``` so instead in this case it would be log n * n for the outer loop ```for i in range(n):```


c)O(2n) reduced to O(n)
* This will run 2 times as long as n or ```bunnies``` due to the recursion call back reducing in a way that results in 2n, but 2 does not count so it is O(n)

## Exercise II
##### I would use binary search to do this
### Starting on the top floor, drop egg
* if it breaks, divide floor in half excluding remainder, and go to that floor
* if egg is un broken, I am done all floors pass and this is my highest floor for this building


### On new floor: drop egg:
* if it breaks: new floor = ( top floor - this floor//2) + this floor, then repeat new floor
* if egg is un broken, I am done all floors pass and this is my highest floor for this building

Run time should average out to O(log n) because I using binary to half my tries with each loop, where floor by floor non binary would be O(n)
