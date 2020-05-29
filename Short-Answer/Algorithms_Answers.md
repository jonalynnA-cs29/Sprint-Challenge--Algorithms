#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n): will run (n) times until the while condition is no longer true


b)O(n^3):first three nested loops are O(n) runtime and
the last loop is not controlled by the input size so it would be constant. The three loops that are controlled by n dictate the overall runtime so O(n^3).


c) O(n): it will run however many times (n) is, until it gets to the base case

## Exercise II

<!-- total_floors = number of stories 
broken_eggs = count of eggs broken
floor = current floor
start at floor 0 and += 1 current floor until floor = total_floors
while floor < total floors
  at each floor do broken_egg count
  if current floor is <= f then broken_eggs = 0
  if current floor is > f broken_eggs += 1

time complexity: O(n) because this function is going to run n times (if total floors is 10 it will run 10 times) -->

changing my answer to this question because after reading the question for the 1000th time I realized I didn't understand the question when I wrote the above(stupid me)

Search for floor f (death of eggs floor)
Binary search instead of linear search
ground floor up to highest floor(sorted from 0-n)
start at the middle floor and drop an egg
  if the egg breaks you are too high
  if the egg does not break you have not reached the death of eggs floor
    if the egg broke go down to the middle floor between current floor and ground floor
    if the egg did not break go up to the middle floor between current floor and highest floor
  repeat this until you find floor f

  time complexity: 
  worst case binary search would be O(log n)
  best case binary search would be O(1)


