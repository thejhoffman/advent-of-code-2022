# advent-of-code-2022

I am using this readme as a journal of sorts as I complete the puzzles for [Advent of Code 2022](https://adventofcode.com/)

I found out about this challenge from another cohort mate in a coding boot camp I am currently attending.

I will graduate from the boot camp around the the same time that this event is over. It should be good practice for preparing for interviews.

I am going to do my best to log any notes/findings from attempting each day's puzzle.

### Day 1
Nothing too much to note. This was the first time actually loading data from a file using python. So it was nice to gain exposure on how to complete that task. Looking at other solutions, after solving my own, I want to try a slightly different method to read the input, or maybe event start using this library I found on reddit. [https://github.com/wimglenn/advent-of-code-data](https://github.com/wimglenn/advent-of-code-data)

Other concepts I encountered while working on today's puzzle.
* The many different ways a list could be copied and the difference between a shallow and deep copy.
  * Resource: [Stack Overflow - How do i clone a list](https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment)
* The use of python's heap queue implementation to find nth larges elements:
  * Resource: [Stack Overflow - Get the second largest number](https://stackoverflow.com/questions/16225677/get-the-second-largest-number-in-a-list-in-linear-time)

### Day 2
Today's puzzle was significantly harder than yesterday's. It gave me the opportunity to try out python 3.10's `match` feature. My resulted still ended up looking like a giant if-else mess, but I was still able to get the result and solve the puzzle.

I believe my solution can be refactored heavily, but am unsure how to start doing so. I am going to look at other solutions online to try and find if there was an easier more elegant way to obtain the answer.

After watching [this youtube video](https://www.youtube.com/watch?v=gLlj_P8edJY), I did refactor my solution in a similar way. My refactor is structured nearly the same as my first solution, but it uses more helper functions. The readability is improved and it is more clear what is going on now.

### Day 3
I was up past midnight on a weekend so I decided to do this puzzle closer to its actual release. I felt more comfortable this time around, having experienced the previous two puzzles already. I wrote a lot better code out of gate. Breaking down parts of the logic into their own functions helped with not having messy code upfront.

I did refactor a function after getting the requirements for part 2 into a function that works for both parts of the puzzle. I also used a helper function found on [Stack OverFlow](https://stackoverflow.com/a/434328) for helping with grouping elements into chunks of a set size inside of a list.

### Day 4
Not much to say for today's puzzle. I believe I have found a good rhythm fow now. I did not run into many hurdles on this puzzle. Getting the data into the shape that I wanted was probably the hardest thing.

One new thing I did learn after going back to look at other solutions for day 3, is python's built in [intersection](https://www.w3schools.com/python/ref_set_intersection.asp) function. This function would also be applicable for today's problem as well. I may considering using it going forward.

I did some more research and found [an article](https://betterprogramming.pub/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41) showcasing more methods of comparing sets in python. I ending implementing an alternate solution using both `issubset` and `intersection` for this puzzle.
